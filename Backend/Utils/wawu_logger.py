import logging
import logging.config

from Utils import ConfigType, WawuConfig


def logger_init():
    logging.config.dictConfig(config=WawuConfig("./Data/LogConfig.yaml", ConfigType.yaml).get_config())
