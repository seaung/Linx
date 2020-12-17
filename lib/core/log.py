import sys
import logging

from lib.core.enums import CUSTOM_LOGGING

logging.addLevelName(CUSTOM_LOGGING.INFO, "+")
logging.addLevelName(CUSTOM_LOGGING.SUCCESS, "*")
logging.addLevelName(CUSTOM_LOGGING.ERROR, "-")
logging.addLevelName(CUSTOM_LOGGING.WARNING, "!")

LOGGER_HANDLER = None

try:
    from ansistrm.ansistrm import ColorizingStreamHandler

    disableColor = False
    for arg in sys.argv:
        if "disable-col" in arg:
            disableColor = True
            break

    if disableColor:
        LOGGER_HANDLER = logging.StreamHandler(sys.stdout)
    else:
        LOGGER_HANDLER = ColorizingStreamHandler(sys.stdout)
        LOGGER_HANDLER.level_map[logging.getLevelName("+")] = (None, "green", False)
        LOGGER_HANDLER.level_map[logging.getLevelName("*")] = (None, "cyan", False)
        LOGGER_HANDLER.level_map[logging.getLevelName("-")] = (None, "red", False)
        LOGGER_HANDLER.level_map[logging.getLevelName("!")] = (None, "yellow", False)
except ImportError:
    LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

FORMATTER = logging.Formatter("")
LOGGER_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(LOGGER_HANDLER)
LOGGER.setLevel(logging.INFO)
