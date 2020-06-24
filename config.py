import json


class Config:
    def __init__(self):
        config_str = ""
        with open('config.json') as f:
            config_str = f.read()

        self.__configs = json.loads(config_str)

    def get_configs(self):
        return self.__configs
