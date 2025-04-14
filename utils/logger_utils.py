import logging
import os

def find_log_dir(base_dir):
    """Ищет папку, заканчивающуюся на '_log' в указанной директории."""
    for entry in os.listdir(base_dir):
        full_path = os.path.join(base_dir, entry)
        if os.path.isdir(full_path) and entry.endswith('_log'):
            return full_path
    return None  # Если не нашлось — можно обработать

def setup_logger(name: str, log_dir: str) -> logging.Logger:
    """Создаёт и настраивает логгер Python под конкретный тест"""

    os.makedirs(log_dir, exist_ok=True)  # Без проверки — сразу создаём, если нет

    log_file = os.path.join(log_dir, f"{name}_code.log")

    # Чтобы не дублировать логи, удалим старый файл, если есть
    if os.path.isfile(log_file):
        os.remove(log_file)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Удалим старые хендлеры, если вдруг фикстура вызывалась повторно
    if logger.hasHandlers():
        logger.handlers.clear()

    # Новый хендлер
    handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

def setup_logger_device(name: str, log_dir: str):
    log_file = os.path.join(log_dir, f"{name}_device.log")

    if os.path.exists(log_file):
        os.remove(log_file)

    return log_file