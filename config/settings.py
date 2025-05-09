import os
import re
import subprocess
import warnings
from typing import Dict, List


class Config:
    """Конфигурация проекта"""
    # Добавляем базовые порты
    BASE_APPIUM_PORT = 4723
    BASE_SYSTEM_PORT = 8200
    BASE_MJPEG_PORT = 9100

    # Путь к APK-файлу
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    APP_PATH = os.path.join(PROJECT_ROOT, "apk", "app-alpha-debug.apk")

    # Пакет и активности
    APP_PACKAGE = "org.wikipedia.alpha"
    APP_ACTIVITY = "org.wikipedia.main.MainActivity"

    # Кэш для устройств
    _devices = None

    @classmethod
    def get_connected_devices(cls) -> List[Dict]:
        """Ленивая загрузка подключенных устройств"""
        if cls._devices is None:
            cls._devices = cls._detect_devices()
        return cls._devices

    @staticmethod
    def _detect_devices() -> List[Dict]:
        """Определяет подключенные устройства через adb"""
        try:
            result = subprocess.run(
                ['adb', 'devices'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=10
            )
            devices = []
            for i, line in enumerate(result.stdout.strip().split('\n')[1:]):
                if match := re.match(r'^(\S+)\s+device$', line):
                    devices.append({
                        "platformName": "Android",
                        "automationName": "uiautomator2",
                        "deviceName": f"device_{i}",
                        "udid": match.group(1),
                        "systemPort": Config.BASE_SYSTEM_PORT + i,
                        "mjpegServerPort": Config.BASE_MJPEG_PORT + i,
                        "appiumPort": Config.BASE_APPIUM_PORT + i,
                        "appPackage": "org.wikipedia.alpha",
                        "appActivity": "org.wikipedia.main.MainActivity"
                    })
            return devices
        except Exception as e:
            warnings.warn(f"Ошибка обнаружения устройств: {str(e)}")
            return []

    @classmethod
    def get_device_config(cls, worker_id: str) -> Dict:
        """Возвращает конфиг для конкретного воркера с проверкой"""
        devices = cls.get_connected_devices()

        if not devices:
            raise RuntimeError("❌ Нет подключенных устройств. Запустите эмуляторы!")

        worker_num = 0 if worker_id == "master" else int(worker_id.replace("gw", ""))

        if worker_num >= len(devices):
            warnings.warn(f"Недостаточно устройств для worker {worker_num}. Используется device 0")
            return devices[0]

        return devices[worker_num]