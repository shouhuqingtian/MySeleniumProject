# -*- coding:utf-8 -*-
import os
import time


# 定义位置存储
def local_doc():
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return path


# 装换为年月日时分秒时间的字符串
def strtime():
    t = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    return t
