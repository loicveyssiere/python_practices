import os
import sys
import configparser
from .logger import logger


class Config:
    def __init__(self):
        if hasattr(sys, '_MEIPASS'):
            logger.debug('running in a PyInstaller bundle')
            os.chdir(sys._MEIPASS)
        else:
            logger.debug('running in a normal Python process')

        self.config_path = os.environ.get("CONFIG", "config/dev.conf")
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path, encoding='utf-8')

    def get(self, section, key):
        if section not in self.config:
            return None

        if key not in self.config[section]:
            return None

        return self.config[section][key]

    def describe(self):
        print("===============================================================")
        print(" CONFIGURATION provided by {}".format(self.config_path))
        print("---------------------------------------------------------------")
        for section in self.config:
            print("o {}".format(section))
            for key in self.config[section]:
                print("  - {}: {}".format(key, self.get(section, key)))
            print("---------------------------------------------------------------")
        print("===============================================================")


# Instantiate for singleton
config = Config()
