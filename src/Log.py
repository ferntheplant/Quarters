import sys
import functools


class LogLevel:
    SPAM = 1
    DEBUG = 2
    INFO = 3
    WARNING = 4
    ERROR = 5
    FATAL = 6

    level_to_string = {
        1: "SPAM",
        2: "DEBUG",
        3: "INFO",
        4: "WARNING",
        5: "ERROR",
        6: "FATAL",
    }


def register_source(source_name):
    pass


def valid_source(source):
    pass


def log(source, level, method, message):
    # TODO: append output to a real logfile
    level = LogLevel.level_to_string[level]
    print("{}\t{}\t{}\t{}".format(source, level, method, message))


def inject_logging(obj, source):
    obj.spam = make_logger(source, LogLevel.SPAM)
    obj.debug = make_logger(source, LogLevel.DEBUG)
    obj.info = make_logger(source, LogLevel.INFO)
    obj.warning = make_logger(source, LogLevel.WARNING)
    obj.error = make_logger(source, LogLevel.ERROR)
    obj.fatal = make_logger(source, LogLevel.FATAL)


def make_logger(source, level):
    return functools.partial(log, source, level, sys._getframe(2).f_code.co_name)
