import logging

#Custom Logger Function That Takes One Argument - File Path
def my_logger(log_path):
    logging.basicConfig(filename=log_path, level=logging.DEBUG, format="%(asctime)s::%(lineno)d::%(message)s")
    logger = logging.getLogger()
    logger.debug("Working")
    return logger
