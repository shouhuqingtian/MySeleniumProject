# -*- coding:utf-8 -*-
import datetime
import logging.handlers
from util import utils

logger = utils.get_logger()
logger.debug('debug message')
logger.info('info')
logger.warning('waring message')
logger.error('error message')
logger.critical('critical message')