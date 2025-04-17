import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name: str, log_dir: str) -> logging.Logger:
    """Создаёт и настраивает логгер Python под конкретный тест"""

    os.makedirs(log_dir, exist_ok=True)  # Без проверки — сразу создаём, если нет

    log_file = os.path.join(log_dir, f"{name}.log")

    # Чтобы не дублировать логи, удалим старый файл, если есть
    if os.path.isfile(log_file):
        os.remove(log_file)

    logger = logging.getLogger(name)
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

    logger.addHandler(file_handler)

    return logger

def setup_logger_device(name: str, log_dir: str):
    log_file = os.path.join(log_dir, f"{name}_device.log")

    if os.path.exists(log_file):
        os.remove(log_file)

    return log_file

def setup_service_logger(test_name: str, log_dir: str) -> logging.Logger:
    log_file = os.path.join(log_dir, f"{test_name}_service.log")

    if os.path.isfile(log_file):
        os.remove(log_file)

    logger = logging.getLogger(f"{test_name}_service")
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()

    handler = logging.FileHandler(log_file, encoding='utf-8', mode='w')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger