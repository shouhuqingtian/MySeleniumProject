# -*- coding:utf-8 -*-
import unittest


class Test01(unittest.TestCase):
    def setUp(self) -> None:
        print('setup...')

    def test01(self):
        print('test01')
        self.assertEqual(1 + 2, 3, '答案正确，测试通过')

    def test02(self):
        print('test02')
        self.assertEqual(5, 4, '答案错误')

    def ti(self):
        print('ti')

    def tearDown(self) -> None:
        print('tearDown...')


if __name__ == '__main__':
    unittest.main
