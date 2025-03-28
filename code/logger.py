import logging
import os

class Logger:
    def __init__(self, project_name):
        self.project_name = project_name
        
        # Get the absolute path of the project's root directory (one level up)
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        log_dir = os.path.join(base_dir, "log")
        self.log_path = os.path.join(log_dir, f"{self.project_name}.log")

        # Ensure the log directory exists
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        # Ensure the log file exists
        if not os.path.exists(self.log_path):
            with open(self.log_path, 'a', encoding="utf-8") as f:
                pass  # Create an empty log file if it doesn’t exist

        # Configure logging
        self.logger = logging.getLogger(self.project_name)
        self.logger.setLevel(logging.DEBUG)  # Capture all levels

        # Create a file handler
        file_handler = logging.FileHandler(self.log_path, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)

        # Create a formatter
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

        # Avoid duplicate handlers
        if not self.logger.hasHandlers():
            self.logger.addHandler(file_handler)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)

    def critical(self, message):
        self.logger.critical(message)