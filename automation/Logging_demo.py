import logging

logging.basicConfig(filename="/Users/shiv/PycharmProjects/automation/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

logging.debug("debug message")
logging.info("Info")
logging.warning("warning warning")
logging.error("error message")
logging.critical("critical message")
