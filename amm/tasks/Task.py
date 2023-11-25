from multiprocessing import process


class Task(process):
    """
    Task Parent class to be used by tasks which are managed by TaskManager.
    """
