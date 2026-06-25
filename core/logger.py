import logging
import sys

class AegisFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    green = "\x1b[32;20m"
    reset = "\x1b[0m"
    format_str = "%(asctime)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + "[+] " + format_str + reset,
        logging.INFO: green + "[✓] " + format_str + reset,
        logging.WARNING: yellow + "[!] " + format_str + reset,
        logging.ERROR: red + "[-] " + format_str + reset,
        logging.CRITICAL: bold_red + "[-] " + format_str + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

def setup_logger():
    logger = logging.getLogger("AegisLogger")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(AegisFormatter())
    logger.addHandler(ch)
    return logger

logger = setup_logger()