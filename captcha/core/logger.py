import logging


class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.log_level = "DEBUG"

        self.logger.setLevel(self.log_level)

        logging.addLevelName(logging.CRITICAL, "[critic]:")
        logging.addLevelName(logging.ERROR, "[error]:")
        logging.addLevelName(logging.WARNING, "[warn]:")
        logging.addLevelName(logging.INFO, "[info]:")
        logging.addLevelName(logging.DEBUG, "[debug]:")
        format_str = "%(asctime)s %(levelname)-10s %(message)s"
        date_format = "%Y-%m-%d %H:%M:%S"

        formatter = logging.Formatter(format_str, date_format)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(self.log_level)
        self.logger.addHandler(stream_handler)

    def get_logger(self):
        return self.logger


# Instantiate for singleton
logger = Logger("default").get_logger()
