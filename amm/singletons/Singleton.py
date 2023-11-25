class Singleton(object):
    """
    Base Singleton class
    """
    instance = None

    def __new__(cls, class_name):
        if not hasattr(cls, 'instance'):
            cls.instance = super(class_name, cls).__new__(cls)
        return cls.instance
