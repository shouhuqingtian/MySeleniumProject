# -*- coding:utf-8 -*-
import logging
import pytest

my_format = '%(asctime)s-%(filename)s-%(module)s-%(lineno)d'
logging.basicConfig(
    filename='my.log',
    filemode='w',
    level=logging.DEBUG,
    format=my_format
)
logging.info('info')
logging.debug('debug')
logging.error('error')
logging.critical('critical')
logging.warning('warning')
