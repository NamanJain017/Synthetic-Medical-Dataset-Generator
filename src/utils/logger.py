import logging
import sys
import os
from pathlib import Path

def setup_logger(name="synthetic_med", log_file="app.log", level=logging.INFO):
    """
    Configures a unified console + file logger for the project.
    """
    logger = logging.getLogger(name)
    
    # Avoid duplicate handlers if setup is called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()
        
    logger.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File Handler
    if log_file:
        # Create outputs directory if it doesn't exist
        log_dir = Path("outputs")
        log_dir.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_dir / log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

def get_logger(name="synthetic_med"):
    """
    Returns the configured logger.
    """
    return logging.getLogger(name)
