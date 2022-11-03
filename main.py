# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press Ctrl+F8 to toggle the breakpoint.
import os

# src, dst, db
# normalize, trim

# filename/path format:
# move prefix, move first name, sort by initial,

# meta tags:
# decade, AMM version/build info, lyrics, album art,
########################################################################################################################
from lib import path_scanner


def __main__():
    path = os.curdir


    phase0(path)


def phase0(path):
    path_scanner(path)


if __name__ == '__main__':
    __main__()
