import os, Singleton


class FileSystem(Singleton):
    """
    :version: 0.0.0
    :author:  Mattijs Snepvangers pegasus.ict@gmail.com
    """

    ###########################################################################
    def __new__(cls):
        return super().__new__(FileSystem)


def run_fast_scan_dir(base_path: str, ext: list = (), clean: bool = False):
    """
    Parses directory (tree) and returns usable files according to extension filter and
    optionally removes any files not included in the filter

    TODO: what happens if filelist exceeds physical capabilities?

    :param base_path: string        Base path to start scan from
    :param ext: list: [ string ]    List of extension to report and retain
    :param clean:                   Remove any files whose extension is not listed in ext
                                    !!! USE WITH CARE !!!

    :return:        folders: list, files: list
    """
    folders, files = [], []

    for f in os.scandir(base_path):
        if f.is_dir(follow_symlinks=False):
            folders.append(f.path)
        elif f.is_file(follow_symlinks=False):
            if ext.__len__() < 1 or os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)
            elif clean and os.path.splitext(f.name)[1].lower() not in ext:
                os.remove(f)

    # for path in list(folders):
    #     sf, f = run_fast_scan_dir(path, ext, clean)
    #     folders.extend(sf)
    #     files.extend(f)
    return folders, files
