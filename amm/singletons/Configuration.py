from configargparse import IniConfigParser as IniParser, ArgumentParser as ArgParser

from amm.MultiVal import *
import Singleton


class Configuration(Singleton):
    """
    :version: 0.0.0
    :author:  Mattijs Snepvangers pegasus.ict@gmail.com
    """
    cfg = None
    syspath = '/etc/amm'
    userpath = '~/.local/share/amm/'
    file = 'config.ini'

    def __new__(cls):
        return super().__new__("Configuration")

    def __init__(self):
        self.args = None
        self.sections = ('main', 'formatting', 'paths')
        self.parse_ini()
        self.parse_args()

    def parse_ini(self):
        with open(self.syspath + self.file) as f:
            cfg1data = f.read()
        with open(self.userpath + self.file) as f:
            cfg2data = f.read()
        parser = IniParser(self.sections, True)
        cfg1 = parser.parse(stream=cfg1data)
        cfg2 = parser.parse(stream=cfg2data)

        self.cfg = cfg1.__dict__ | cfg2.__dict__

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

    def load(self, filename: str = userpath + file):
        """
        :param filename:
        :return:
        """
        pass

    def save(self, filename: str = userpath + file):
        """
        :param filename:
        :return:
        """
        pass

    def parse_args(self):
        """
        Argument parser
        arguments:
            > -n / --new    starts new instance with clean database etc
            > --ui=[t/g]    start TUI or GUI, default: daemon mode
            > -h / --help
            > -u / --update force update software & database to latest version,
                            even if current version is latest already
        :return:
        """
        parser = ArgParser()
        self.args = parser.parse_args()
