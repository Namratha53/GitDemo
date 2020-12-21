import logging

def test_logging():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatterobj = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s %(message)s")
    fileHandler.setFormatter(formatterobj)
    logger.addHandler(fileHandler)  #filehandler object
    logger.setLevel(logging.ERROR)
    logger.debug("Debug log s executed")
    logger.info("Info log is being printed")
    logger.warning("Warning is pinted but test case still excuted")
    logger.error("Major error occured")
    logger.critical("Critical issue")


