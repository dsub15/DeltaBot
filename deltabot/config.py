import json
import os


class Config(object):
    """
    Holds the configuration options for the bot
    """
    def __init__(self, config_file):
        if isinstance(config_file, dict):
            self.attrs = config_file
        elif os.path.isfile(config_file):
            self.attrs = json.load(open(config_file))
        else:
            self.attrs = json.loads(config_file)

    def __getattr__(self, name):
        return self.attrs.get(name)

    def __getitem__(self, name):
        return self.attrs.get(name)