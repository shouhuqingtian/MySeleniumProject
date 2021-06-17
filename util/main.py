# -*- coding:utf-8 -*-
from testcases import testcase01, testcase02
from util.utils import *
from selenium import webdriver
from testcases.basic.test_user_register import TestUserRegister

if __name__ == '__main__':
    # testcase01.test02()
    # testcase02.test01()
    # driver = webdriver.Firefox()
    # driver.get('https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx')
    # driver.maximize_window()
    # print(get_code(driver, 'imgCode'))
    case = TestUserRegister()
    case.test_register_code_error()
    case.test_register_ok()

