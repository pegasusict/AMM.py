from typing import Dict


def check_socket() -> bool:
    import os
    return False


class TaskManager:
    """
    :version: 0.0.0
    :author:  Mattijs Snepvangers pegasus.ict@gmail.com
    """

    states: dict[str, int] = {
        "imported": 0,
        "fp": 1,
        "mbid": 2,
        "tags": 4,
        "albumart": 8,
        "lyrics": 16,
        "trimmed": 32,
        "normalized": 64
    }

    taskIDs: dict[str, int] = {
        "importer": 100,
        "mbfp": 200,
        "dedup": 300,
        "mbq": 400,
        "artget": 500,
        "lyricsget": 600,
        "trimmer": 700,
        "normalizer": 800
    }

    runningTasks = {}

    def task_running(self, task_id):
        return self.runningTasks.__contains__(task_id)

    instance = None  # class singleton instance

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TaskManager, cls).__new__(cls)
        return cls.instance
