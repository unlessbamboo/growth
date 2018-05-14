# coding:utf8
"""
参考django进行日志配置, 利用LOGGERS来添加日志配置
"""

import logging
import logging.config
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 是否DEBUG
DEBUG = False


# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': ("%(levelname)s %(asctime)s %(module)s "
                       "%(filename)s:%(lineno)s "
                       "%(process)d %(thread)d %(message)s")
        },
    },
    'filters': {},
    'handlers': {},
    'loggers': {},
}

# 自定义 Logger 配置, 之后可以在代码的任何地方添加如下代码进行日志记录:
# my_logger = logging.getLogger('name-1')
# my_logger.error('message')
LOGGERS = ["common", "error", "info"]
for name in LOGGERS:
    handler = {
        'level': 'INFO',
        # 利用TimedRotatingFileHandler来按照日期切割
        'class': 'logging.handlers.TimedRotatingFileHandler',
        'filename': os.path.join(BASE_DIR, 'logs/%s.log' % name),
        'formatter': 'verbose',
        'when': 'M',
    }
    logger = {
        'handlers': [name],
        'level': 'INFO',
        'propagate': True,
    }
    LOGGING['handlers'][name] = handler
    LOGGING['loggers'][name] = logger

# 是否开启调试
if DEBUG:
    LOGGING['handlers']['console'] = {
        'level': 'DEBUG',
        'class': 'logging.StreamHandler',
        'formatter': 'verbose'
    }
    for logger in LOGGING['loggers']:
        LOGGING['loggers'][logger]['handlers'] = ['console']


# 启动配置
logging.config.dictConfig(LOGGING)
logger_error = logging.getLogger('error')
logger_info = logging.getLogger('info')
