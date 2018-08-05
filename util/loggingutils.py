import logging


def init_logger(logfile='main.log', mode='a', to_stdout=True):
    logger = logging.getLogger('dhl')
    if logfile is not None:
        fh = logging.FileHandler(logfile, mode=mode)
        fmt = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s - %(message)s',
                                datefmt='%y-%m-%d %H:%M:%S')
        fh.setFormatter(fmt)
        logger.addHandler(fh)
    if to_stdout:
        logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
    return logger
