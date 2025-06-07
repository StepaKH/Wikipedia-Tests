import subprocess

from fastapi import BackgroundTasks, FastAPI

from bot.utils.test_runner import run_tests

app = FastAPI()

@app.post("/ci/trigger")
async def trigger_tests(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_ci_pipeline)
    return {"status": "pipeline_started"}

async def run_ci_pipeline():
    # 1. "Собираем" проект
    build_log = subprocess.run(["echo", "Building..."], capture_output=True)

    # 2. Запускаем тесты
    test_result = await run_tests()

    # 3. "Деплоим"
    deploy_log = subprocess.run(["echo", "Deploying..."], capture_output=True)

    return {
        "build": build_log.stdout.decode(),
        "tests": test_result,
        "deploy": deploy_log.stdout.decode()
    }