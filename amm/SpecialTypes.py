class ReadOnlyDict(dict):
    def __setitem__(self, key, value):
        raise RuntimeError("Modification not supported")
