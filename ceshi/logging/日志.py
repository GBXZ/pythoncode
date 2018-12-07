
#
# LOG_FORMAT = '%(asctime)s - %(levelname)s - %(thread)d - %(message)s'
# logging.basicConfig(filename='my.log', level=logging.ERROR, format=LOG_FORMAT)
# # 创建一个简单的日志
# logging.debug('this is a debug log')
# logging.info('this is a info log')
# logging.warning('this is a warning log')
# logging.error('this is error log')
# logging.critical('this is a critical')
# # 创建一个简单的日志另一种形式
# # logging.log(logging.DEBUG, 'this is a debug log')
# # logging.log(logging.INFO, 'this is a info log')
# # logging.log(logging.WARNING, 'this is a warning log')
# # logging.log(logging.ERROR, 'this is a error log')
# # logging.log(logging.CRITICAL, 'this is a critical log')

# all_log = logging.Logger('mylog')
# all_log_fomatte = logging.Formatter(fmt='%(actime)s - %(levelname)s - %(message)s')
# all_log_handler = logging.Handler()
# all_log_handler.setLevel(level=logging.DEBUG)
# all_log_handler.setFormatter(fmt=all_log_fomatte)
# all_log.addHandler(all_log_handler)
# logging.debug('i am a debug log')

import logging
import logging.handlers
import datetime

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')




