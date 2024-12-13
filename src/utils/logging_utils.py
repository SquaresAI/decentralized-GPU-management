import logging

class LoggingUtils:
    """Class for managing logging configuration and log messages."""

    @staticmethod
    def setup_logging(log_file="app.log", level=logging.INFO):
        """Sets up the logging configuration."""
        logging.basicConfig(
            filename=log_file,
            level=level,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        logger = logging.getLogger()
        logger.info("Logging initialized.")
        return logger

    @staticmethod
    def log_event(logger, message, level=logging.INFO):
        """Logs a specific event."""
        if level == logging.INFO:
            logger.info(message)
        elif level == logging.WARNING:
            logger.warning(message)
        elif level == logging.ERROR:
            logger.error(message)
        else:
            logger.debug(message)

# Example usage
if __name__ == "__main__":
    logger = LoggingUtils.setup_logging("gpu_management.log")
    LoggingUtils.log_event(logger, "GPU node initialized.", logging.INFO)
    LoggingUtils.log_event(logger, "GPU node under high load.", logging.WARNING)
