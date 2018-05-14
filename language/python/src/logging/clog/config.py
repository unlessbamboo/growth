# coding:utf8
"""
参考django进行日志配置, 利用LOGGERS来添加日志配置
"""

import os
import logging
import logging.config
from .clogconfig import clogDictConfig

ROTATEHANDLER = 'clogtimehandler.ConcurrentTimeRotatingFileHandler'
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.realpath(__file__))))
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
# 利用ConcurrentLogHandler来完成多进程的日志写入操作
# https://pypi.org/project/ConcurrentLogHandler/0.9.1/
LOGGERS = ["common", "error", "info"]
for name in LOGGERS:
    handler = {
        'level': 'INFO',
        'class': ROTATEHANDLER,
        'filename': os.path.join(BASE_DIR, 'logs/%s.log' % name),
        'formatter': 'verbose',
        'when': 'm',
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
clogDictConfig(LOGGING)
logger_error = logging.getLogger('error')
logger_info = logging.getLogger('info')
