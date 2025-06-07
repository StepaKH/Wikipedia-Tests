import asyncio
import json
import shutil
import time
from pathlib import Path

import psutil

HTML_DIR = Path("reports/html")
_current_process = None  # Глобальная переменная для управления процессом

_is_running = False

def is_tests_running() -> bool:
    return _is_running

def get_test_stats():
    passed = failed = skipped = 0
    allure_results = Path("allure")

    for result_file in allure_results.glob("*.json"):
        with open(result_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            status = data.get("status")
            if status == "passed":
                passed += 1
            elif status == "failed" or status == "broken":
                failed += 1
            elif status == "skipped":
                skipped += 1

    return passed, failed, skipped

def extract_failed_tests() -> str:
    allure_results = Path("allure")
    failed_tests = []

    for result_file in allure_results.glob("*.json"):
        try:
            with open(result_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                status = data.get("status", "").lower()

                if status in ("failed", "broken"):
                    name = data.get("name", "Unknown test")
                    failed_tests.append(f"🔴 {name}")
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print(f"⚠️ Ошибка чтения файла {result_file}: {str(e)}")
            continue

    return "\n".join(failed_tests) if failed_tests else ""

async def run_tests(parallel_count: int = 1, marker: str = None) -> tuple[str, bool, str, dict]:
    global _current_process, _is_running

    # Стартовые метрики
    start_time = time.time()
    cpu_start = psutil.cpu_percent(interval=None)
    ram_start = psutil.virtual_memory().percent

    shutil.rmtree(HTML_DIR, ignore_errors=True)

    cmd = [
        "pytest",
        "--tb=short",
        "-ra",
        "--alluredir=allure",
    ]
    if marker:
        cmd.extend(["-m", marker])

    if parallel_count > 1:
        cmd.extend(["-n", str(parallel_count)])

    if _is_running:
        return "⚠️ Тесты уже выполняются, дождитесь завершения.", False, "", {}

    _is_running = True
    try:
        _current_process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await _current_process.communicate()
        _current_process = None

        # Генерация HTML отчета
        gen_cmd = ["allure", "generate", "allure", "-o", str(HTML_DIR), "--clean"]
        gen_proc = await asyncio.create_subprocess_exec(*gen_cmd)
        await gen_proc.communicate()

        test_duration = time.time() - start_time
        cpu_avg = psutil.cpu_percent(interval=None)
        ram_avg = psutil.virtual_memory().percent

        # Собираем статистику
        resource_stats = {
            "duration": round(test_duration, 2),
            "cpu": cpu_avg,
            "ram": ram_avg,
            "cpu_diff": round(cpu_avg - cpu_start, 2),
            "ram_diff": round(ram_avg - ram_start, 2)
        }

        passed, failed, skipped = get_test_stats()
        failed_tests = extract_failed_tests()
        success = not failed_tests

        msg = (
            f"📊 Результаты тестов:\n"
            f"🟢 Пройдено: {passed}\n"
            f"🔴 Упало: {failed}\n"
            f"🟡 Пропущено: {skipped}\n\n"
            f"{'✅ Все тесты прошли успешно!' if success else '❌ Есть упавшие тесты!'}"
        )

        return msg, success, failed_tests, resource_stats

    except Exception as e:
        _current_process = None
        return f"❌ Ошибка запуска тестов: {str(e)}", False, "", {}

    finally:
        _is_running = False

async def stop_tests():
    global _current_process, _is_running

    try:
        if _current_process and _current_process.returncode is None:
            _current_process.terminate()
            await _current_process.wait()
            return True
        return False
    finally:
        _current_process = None
        _is_running = False