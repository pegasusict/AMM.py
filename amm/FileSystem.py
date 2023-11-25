import os

class FileSystem:

  """
  :version:0.0.0
  :author:Mattijs Snepvangers
  """

def run_fast_scandir(path, ext=''):  # dir: str, ext: list
    subfolders, files = [], []

    for f in os.scandir(path):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)

    for path in list(subfolders):
        sf, f = run_fast_scandir(path, ext)
        subfolders.extend(sf)
        files.extend(f)
    return subfolders, files
