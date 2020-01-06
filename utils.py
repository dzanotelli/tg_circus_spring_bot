import configparser
import logging
import os

from exceptions import CircuSpringBotConfError


log = logging.getLogger(__name__)


def init_logger(dev_mode=False):
    # formatters
    fmt = "%(asctime)s [%(levelname)s:%(module)s:%(lineno)d] %(message)s"
    formatter = logging.Formatter(fmt=fmt)

    # handlers
    h = logging.StreamHandler()
    h.setLevel(logging.DEBUG)
    h.setFormatter(formatter)

    # loggers
    logger = logging.getLogger(__name__)
    logger.addHandler(h)

    if dev_mode:
        for h in logger.handlers:
            h.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)

    return logger


def read_config():
    parser = configparser.ConfigParser()
    conf_path = os.environ.get('CS_BOT_CONFIG_FILE', 'config.ini')
    parser.read(conf_path)
    return parser
