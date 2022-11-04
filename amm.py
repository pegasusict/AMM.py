#!/usr/bin/python3

try:
    from amm.tagger import main
    main('/usr/share/locale', False)
except SystemExit:
    raise  # Just continue with a normal application exit
except:  # noqa: E722,F722 # pylint: disable=bare-except
    from amm import crash_handler
    crash_handler()
    raise
