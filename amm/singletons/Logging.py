from amm.SpecialTypes import ReadOnlyDict as RODict
import Singleton


class LogLevel:
    _levels = {
        10: "CRITICAL", 20: "ERROR", 30: "WARNING", 40: "NOTICE", 50: "INFO", 60: "DEBUG", 70: "TRACE"
    }
    LOG_LEVELS = RODict(_levels)
    _levels_by_name = {v: k for k, v in LOG_LEVELS.items()}
    LEVELS_BY_NAME = RODict(_levels_by_name)


def log(level: int = 20, message: str = "no error message given"):
    """
    Base Logging function which is called by every other function in this module
    :param level:       LOGLEVEL, default to 20 -> ERROR
    :param message:     log message
    :return:            complete logline
    """
    from datetime import datetime
    timestamp: str = datetime.utcnow()
    if level in LogLevel.LOG_LEVELS:
        loglevel = LogLevel.LOG_LEVELS[level]
    else:
        loglevel = LogLevel.LOG_LEVELS[20]

    return timestamp + ' [' + loglevel + ']: ' + message
