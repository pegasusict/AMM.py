import TaskManager
from Configuration import Configuration


class Main:
    """
    :version:0.0.0
    :author:Mattijs Snepvangers <pegasus.ict@gmail.com>
    """

    def __new__(cls):
        pass

    def __init__(self):
        self.socket_state = TaskManager.check_socket()
        # if not self.socket_state:
        self.cfg = Configuration()
