import configparser

class Config:
    def __init__(self, path="config.ini"):
        self.path = path
        self.parser = configparser.ConfigParser()
        self.parser.read(self.path)

    def get(self, section, key):
        return self.parser.get(section, key)
