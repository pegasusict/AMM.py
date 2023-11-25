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

    def __query(self, query: str):
        pass

    def add(self, table: str, data: list):
        pass

    def get(self, get: str, table: str, where: str = None, equals = None):
        qry = "GET " + get + " FROM " + table
        if where:
            qry += " WHERE " + where
        if equals:
            qry += " EQUALS " + equals
        return self.__query(self, qry)

    def get_list(self, get: str, table: str, where: str, equals):
        query = "GET " + get + " FROM " + table

    def update(self, query):
        pass
