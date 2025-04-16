import logging
import os
import sys
from logging.handlers import RotatingFileHandler

def find_log_dir(base_dir):
    """Ищет папку, заканчивающуюся на '_log' в указанной директории."""
    for entry in os.listdir(base_dir):
        full_path = os.path.join(base_dir, entry)
        if os.path.isdir(full_path) and entry.endswith('_log'):
            return full_path
    return None


def get_logger(name=None):
    """Возвращает настроенный логгер с заданным именем"""
    logger = logging.getLogger(name or __name__)

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Консольный вывод
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


def setup_logger(test_name, project_root):
    """
    Настройка логгера с записью в файл
    :param test_name: имя теста (например, 'test_add_or_edit_languages')
    :param project_root: корневая директория проекта
    :return: настроенный логгер
    """
    # Путь к директории логов согласно структуре проекта
    log_dir = os.path.join(project_root, "logs", "onboarding_logs")
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, f"{test_name}.log")

    logger = logging.getLogger(test_name)
    logger.setLevel(logging.DEBUG)

    # Очистка предыдущих handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # Формат логов
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Ротация логов (5 файлов по 5 МБ)
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding='utf-8',
        mode='w'
    )
    file_handler.setFormatter(formatter)

    # Консольный вывод
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def setup_logger_device(name: str, log_dir: str):
    """Настройка логгера для устройств"""
    os.makedirs(log_dir, exist_ok=True)
    return os.path.join(log_dir, f"{name}_device.log")