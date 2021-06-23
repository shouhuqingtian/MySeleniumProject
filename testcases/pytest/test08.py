# -*- coding:utf-8 -*-
import allure
import pytest


@pytest.fixture(scope="session")
def login():
    print('用例先登录')


@allure.step('步骤1：点xxx')
def step_1():
    print('111')


@allure.step('步骤2：点xxx')
def step_2():
    print('222')


@allure.feature('编辑界面')
class TestEditPage():
    """编辑界面"""

    @allure.story('这是一个xxx的用例')
    def test01(self, login):
        """用例描述：先登录，再执行"""
        step_1()
        step_2()
        print('xxx')

    @allure.story('打开a界面')
    def test01(self, login):
        """用例描述：先登录，再执行"""
        print('yyy')


if __name__ == '__main__':
    pytest.main(['--alluredir', './reports', 'test08.py'])
    pytest.main(['--alluredir', './reports', 'test08.py'])
