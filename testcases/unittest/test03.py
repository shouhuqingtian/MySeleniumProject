# -*- coding:utf-8 -*-
import unittest
import os


class MyTestCase03(unittest.TestCase):
    def test01(self):
        print('test01')

    def test02(self):
        print('test02')


class MyTestCase04(unittest.TestCase):
    def test03(self):
        print('test03')

    def test04(self):
        print('test04')


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    # suite.addTest(loader.loadTestsFromTestCase(MyTestCase03))
    # suite.addTest(loader.loadTestsFromTestCase(MyTestCase04))
    # suite.addTest((loader.loadTestsFromModule(MyTestCase03)))
    # suite.addTest((loader.loadTestsFromModule(MyTestCase04)))
    path = os.path.dirname(os.path.abspath(__file__))
    suite.addTest(loader.discover(path))
    runner = unittest.TextTestRunner()
    runner.run(suite)
