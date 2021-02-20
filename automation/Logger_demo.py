import logging

logging.basicConfig(filename="/Users/shiv/PycharmProjects/automation/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p',)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("debug message")
logger.info("Info")
logger.warning("warning warning")
logger.error("error message")
logger.critical("critical message")