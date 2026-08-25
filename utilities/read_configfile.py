import os
from configparser import ConfigParser


def read_configfile(section, key):
    config = ConfigParser()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "..", "ConfigurationData", "conf.ini")
    config.read(config_path)
    return config.get(section, key)
