# -*- coding:utf-8 -*-
import pytest

# 列表
data = ['123', '456']


@pytest.mark.parametrize('pwd', data)
def test(pwd):
    print(pwd)


# 元祖
data2 = [(1, 2, 3), (4, 5, 6)]


@pytest.mark.parametrize('a,b,c', data2)
def test02(a, b, c):
    print(a, b, c)


# 字典
data3 = ({
             'user': '1',
             'ped': '2'
         },
         {
             'age': '3',
             'email': '519328539@qq.com'
         })


@pytest.mark.parametrize('dic', data3)
def test03(dic):
    print(dic)


data_1 = [
    pytest.param(1, 2, 3, id="(a+b):pass"),
    pytest.param(4, 5, 11, id="(a+b):fail"),
]


def add(a, b):
    return a + b


class TestParametrize:
    @pytest.mark.parametrize('a, b, expect', data_1)
    def test_parametrize_1(self, a, b, expect):
        assert add(a, b) == expect
