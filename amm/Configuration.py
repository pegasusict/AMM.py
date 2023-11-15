from configargparse import IniConfigParser

from MultiVal import *


class Configuration(object):
    """
    :version: 0.0.0
    :author:  Mattijs Snepvangers pegasus.ict@gmail.com
    """
    instance = None
    cfg = None
    syspath = '/etc/amm'
    userpath = '~/.amm/'
    file = 'config.ini'

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Configuration, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        sections = ()
        with open(self.syspath+self.file) as f:
            cfg1data = f.read()
        with open(self.userpath+self.file) as f:
            cfg2data = f.read()
        parser = IniConfigParser(sections, True)
        cfg1 = parser.parse(stream=cfg1data)
        cfg2 = parser.parse(stream=cfg2data)

        self.cfg = cfg1.__dict__.update(cfg2.__dict__)

    def get(self, key: str, section: str = 'general'):
        """
        @param string key :
        @param string section :
        @return MultiVal :
        """
        pass

    def set(self, key: str, value: MultiVal = True, typing: MultiVal = bool, section: str = 'general'):
        """
        @param string key :
        @param MultiVal value : can be int/str/bool
        @param MultiVal typing :
        @param string section : optional
        @return bool :
        """
        pass

    def load(self, filename: str = userpath+file):
        """
        :param filename:
        :return:
        """
        pass

    def save(self, filename: str = userpath+file):
        """
        :param filename:
        :return:
        """
        pass

    def parse_args(self):
        """
        :return:
        """
        parser = arg
