# -*- coding:utf-8 -*-
import pytest


class TestCase01:
    @classmethod
    def setup_class(cls):
        print('setup_class')

    def test01(self):
        print('test01')

    @classmethod
    def teardown_class(cls):
        print('setup_class')


def setup_function():
    print('setup_function')


def teardown_function():
    print('teardown_function')


def setup_module():
    print('setup_module')


def teardown_module():
    print('teardown_module')


def test01():
    print('test01')


def test02():
    print('test02')


if __name__ == '__main__':
    pytest.main(['-sv', 'test07.py'])
