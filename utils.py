import configparser
import logging
import os

from exceptions import CircuSpringBotConfError


log = logging.getLogger(__name__)


def init_logger():
    # formatters
    fmt = "%(asctime)s [%(levelname)s:%(module)s:%(lineno)d] %(message)s"
    formatter = logging.Formatter(fmt)

    # handlers
    h = logging.StreamHandler()
    h.setLevel(logging.DEBUG)
    h.setFormatter(fmt)

    # loggers
    logger = logging.getLogger(__name__)
    logger.addHandler(h)

    return logger


def read_config():
    parser = configparser.ConfigParser()
    conf_path = os.environ.get('CS_BOT_CONFIG_FILE', 'config.ini')
    parser.read(conf_path)

    try:
        data = {
            'api_key': parser['telegram']['api_key'],
        }
    except KeyError as e:
        err = f"Bad configuration provided (file {conf_path}). Details: {e}"
        log.error(err)
        raise CircuSpringBotConfError(err)

    return data
