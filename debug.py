from util.loggingutils import init_logger
import datetime
import logging

str_today = datetime.date.today().strftime('%y-%m-%d')
# init_logging('res-{}.log'.format(str_today), mode='w', to_stdout=False)
# logging.info('damn')
logger = init_logger('res-{}.log'.format(str_today), to_stdout=True)
logger.info('foo')
