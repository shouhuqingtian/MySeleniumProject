# -*- coding:utf-8 -*-
import pytest


class TestLoginCase:
    def test01(self):
        print('test01')


if __name__ == '__main__':
    pytest.main(['-s', 'test01.py'])