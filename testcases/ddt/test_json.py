# -*- coding:utf-8 -*-
import pytest
import json


def test_data():
    with open('test_json.json') as file:
        data = []
        lst = json.load(file)
        data.extend(lst["key"])
        return data


@pytest.mark.parametrize('name', test_data())
def test01(name):
    print(name)


if __name__ == '__main__':
    pytest.main(['-sv', 'test_json.py'])
