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

class Logger:
    _logger = None

    @classmethod
    def init(cls):
        if cls._logger is None:
            cls._logger = _create_logger()

    @classmethod
    def get_logger(cls):
        if cls._logger is None:
            raise RuntimeError("Logger is not initialized. Call Logger.init() first.")
        return cls._logger

    @classmethod
    def set_level(cls, level: str | int) -> None:
        cls.get_logger().setLevel(level)

    @classmethod
    def info(cls, message: str) -> None:
        cls.get_logger().info(message)

    @classmethod
    def debug(cls, message: str) -> None:
        cls.get_logger().debug(message)

    @classmethod
    def error(cls, message: str) -> None:
        cls.get_logger().error(message)

    @classmethod
    def step(cls, message: str) -> None:
        cls.get_logger().debug(f"[STEP] {message}")