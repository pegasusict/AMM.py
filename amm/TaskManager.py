
class TaskManager:

  """
  :version:
  :author:
  """

  states = {
    "imported" : 0,
    "fp" : 1,
    "mbid" : 2,
    "tags" : 4,
    "albumart" : 8,
    "lyrics" : 16,
    "trimmed" : 32,
    "normalized" : 64
  }

  taskIDs = {
    "importer" : 100,
    "mbfp" : 200,
    "dedup" : 300,
    "mbq" : 400,
    "artget" : 500,
    "lyricsget" : 600,
    "trimmer" : 700,
    "normalizer" : 800
  }

  def CheckSocket(self):
    import os


  def taskRunning(self, task_id):
    import os

