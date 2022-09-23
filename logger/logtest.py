import logging
from logging import config
from os import path

def get_logger():
    log_file_path = path.join(path.dirname(path.abspath(__file__)), 'log.config')
    config.fileConfig(log_file_path)
    logger = logging.getLogger("tanka")
    print(logger)
    return logger
logger = get_logger()

def addition(a, b):
    logger.debug("Inside Addition Function")
    if isinstance(a, str) and a.isdigit():
        logger.warning("Warning : Parameter A is passed as String. Future versions won't support it.")

    if isinstance(b, str) and b.isdigit():
        logger.warning("Warning : Parameter B is passed as String. Future versions won't support it.")

    try:
        result = float(a) + float(b)
        logger.info("Addition Function Completed Successfully")
        return result
    except Exception as e:
        logger.error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
        return None

if __name__ == "__main__":
    #logger.info("Current Log Level : {}\n".format(logger.getLevel()))
    result = addition(10,20)
    logger.info("Addition of {} & {} is : {}\n".format(10,20, result))

    result = addition("20",20)
    logger.info("Addition of {} & {} is : {}\n".format("'20'",20, result))

    result = addition("A",20)
    logger.info("Addition of {} & {} is : {}".format("A",20, result))