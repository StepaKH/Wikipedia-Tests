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
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, f"{name}_code.log")

    if os.path.exists(log_file):
        os.remove(log_file)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def setup_logger_device(name: str, log_dir: str):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, f"{name}_device.log")

    if os.path.exists(log_file):
        os.remove(log_file)

    return log_file