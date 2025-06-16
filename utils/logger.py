# utils/logger.py
import logging
import sys
from pathlib import Path

def setup_logger(name: str, log_file: str = "bot.log", level=logging.INFO):
    """Set up a logger with both file and console output."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create logs directory if it doesn't exist
    Path("logs").mkdir(exist_ok=True)
    
    # File handler
    file_handler = logging.FileHandler(f"logs/{log_file}")
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    ))
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(
        "%(name)s - %(levelname)s - %(message)s"
    ))
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger
