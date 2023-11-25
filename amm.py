#!/usr/bin/python3

__version__ = [0, 0, 0]
__build__ = [20231100]

try:
    from amm.Main import Main
    Main()
except SystemExit:
    raise  # Just continue with a normal application exit
except:  # noqa: E722,F722 # pylint: disable=bare-except
    from amm.crash_handler import CrashHandler
    # TODO create a decent crash handler
    ch = CrashHandler()
    raise

# check which to start: backend, GUI or TUI
# load config
# connect to DB/backend
# load statuses
# load menu
# load dashboard in case of UI
