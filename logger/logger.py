import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from logger.logger_config import LoggerConfig


def _create_logger():
    if not os.path.isdir(LoggerConfig.LOGS_DIR_NAME):
        os.makedirs(LoggerConfig.LOGS_DIR_NAME)

    logger = logging.getLogger(LoggerConfig.LOGGER_NAME)

    if logger.handlers:  # защита от дублей
        return logger

    logger.setLevel(LoggerConfig.LOGS_LEVEL)

    file_handler = RotatingFileHandler(
        LoggerConfig.LOGGER_FILE_NAME,
        maxBytes=LoggerConfig.MAX_BYTES,
        backupCount=LoggerConfig.BACKUP_COUNT
    )

    console_handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter(LoggerConfig.FORMAT)
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


_logger = _create_logger()


class Logger:

    @staticmethod
    def set_level(level: str | int) -> None:
        _logger.setLevel(level)

    @staticmethod
    def info(message: str) -> None:
        _logger.info(message)

    @staticmethod
    def debug(message: str) -> None:
        _logger.debug(message)

    @staticmethod
    def error(message: str) -> None:
        _logger.error(message)

    @staticmethod
    def step(message: str) -> None:
        _logger.debug(f"[STEP] {message}")