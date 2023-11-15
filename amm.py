#!/usr/bin/python3

try:
    from amm.Main import Main
    Main()
except SystemExit:
    raise  # Just continue with a normal application exit
except:  # noqa: E722,F722 # pylint: disable=bare-except
    from amm.crash_handler import CrashHandler
    ch = CrashHandler()
    raise

# check which to start: backend, GUI or TUI
# load config
# connect to DB/backend
# load statuses
# load menu
# load dashboard in case of UI
