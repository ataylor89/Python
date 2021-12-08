import logging
import mathart

def main():
    # create logger
    logger = logging.getLogger("test2")
    logger.setLevel(logging.INFO)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    fh = logging.FileHandler('test2.log')
    fh.setLevel(logging.INFO)

    # create formatter
    formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")

    # add formatter
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)
	
    logger.info("Started")
    mathart.hexagonspiral()
    logger.info("Finished")

if __name__ == '__main__':
    main()
