# -*- coding:utf-8 -*-
import os
import unittest
from ddt import data, ddt, unpack, file_data


def get_data():
    testdata = [{'name': 'tom', 'age': 20}, {'name': 'kite', 'age': 30}]
    return testdata


@ddt
class MyTestCase(unittest.TestCase):
    # 读取元组数据-单组元素
    @data(1, 2, 3)
    def test01(self, value):
        print(value)

    # 读取元组数据-多组数据
    @data((1, 2, 3), (4, 5, 6))
    def test02(self, value):
        print(value)

    # 读取元组数据-拆分数据
    @data((1, 2, 3), (4, 5, 6))
    @unpack  # 拆分数据
    def test03(self, value1, value2, value3):
        print(value1, value2, value3)

    # 列表
    @data([{'name': 'tom', 'age': 20}, {'name': 'kite', 'age': 30}])
    def test(self, value):
        print(value)

    # 字典
    @data({'name': 'tom', 'age': 20}, {'name': 'kite', 'age': 30})
    def test05(self, value):
        print(value)

    # 字典-拆分
    @data({'name': 'tom', 'age': 20}, {'name': 'kite', 'age': 30})
    @unpack
    def test06(self, name, age):
        print(name, age)

    # 变量或者方法调用
    testdata = [{'name': 'tom', 'age': 20}, {'name': 'kite', 'age': 30}]

    @data(get_data())
    def test07(self, value):
        print(value)

    # 读文件
    @file_data(''.join([os.getcwd(), '/test_json.json']))
    def test08(self, value2):
        print(value2)


if __name__ == '__main__':
    unittest.main()
