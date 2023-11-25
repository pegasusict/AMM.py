import Singleton


class DataBase:
    """
    :version: 0.0.0
    :author:  Mattijs Snepvangers <pegasus.ict@gmail.com>
    """

    def __new__(cls):
        return super().__new__(DataBase)

    def connect(self):
        pass

    def __query(self, query):
        pass

    def add(self, table: str, data: list):
        pass

    def get(self, query):
        pass

    def get_list(self, query):
        pass

    def update(self, query):
        pass
