#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    Copyright 2011 timger
    +Author timger
    +Gtalk&Email yishenggudou@gmail.com
    +Msn yishenggudou@msn.cn
    +Weibo @timger http://t.sina.com/zhanghaibo
    +twitter @yishenggudou http://twitter.com/yishenggudou
    Licensed under the MIT License, Version 2.0 (the "License");
'''

import logging
import logging.handlers
import time
from conf import conf

__author__ = 'timger & yishenggudou@gmail.com'
__license__ = 'MIT'
__version__ = (0, 0, 0)

"""
"""
logging.Formatter.converter = time.gmtime


def setup_custom_logger(name, logfile=None):
    fmt = '''%(asctime)s %(levelname)s %(name)s.%(funcName)s %(lineno)d %(thread)d:%(threadName)s: %(message)s'''
    #fmt = '%(asctime)s - %(levelname)s - %(module)s - %(message)s'
    formatter = logging.Formatter(fmt=fmt)
    
    if logfile is None:
        logfile = conf.rqmrjob_log
        handler = logging.handlers.RotatingFileHandler(logfile,
                                               maxBytes=1024*50*1025,
                                               backupCount=5,
                                                )
    elif logfile == 'stdout':
        handler = logging.StreamHandler()
    else:
        handler = logging.handlers.RotatingFileHandler(logfile,
                                               maxBytes=1024*50,
                                               backupCount=5,
                                               )
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
