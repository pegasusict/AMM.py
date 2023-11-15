class DataBase:
    """
    :version: 0.0.0
    :author:  Mattijs Snepvangers <pegasus.ict@gmail.com>
    """

    instance = None  # class singleton instance

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DataBase, cls).__new__(cls)
        return cls.instance

    def connect(self):
        pass

    def query(self, query):
        pass

    def add(self, table: str, data: list):
        pass
