# -*- coding:utf-8 -*-
import csv
import pytest


def get_data():
    with open('test.csv')as f:
        lst = csv.reader(f)
        data = []
        for i in lst:
            data.extend(i)
        return data


@pytest.mark.parametrize('name', get_data())
def test01(name):
    return name


if __name__ == '__main__':
    # print(get_data())
    pytest.main(['-sv', 'test_csv.py'])
