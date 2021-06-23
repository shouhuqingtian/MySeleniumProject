# -*- coding:utf-8 -*-
import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util import utils
import pytest


class TestAdminLogin:
    # @classmethod
    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://159.75.96.188:18080/jpress/admin/login')
        self.driver.maximize_window()

    # 测试后台登录，用户名错误
    def test_admin_login_username_error(self):
        # 用户名为空
        username = ''
        pwd = '123456'
        code = utils.get_code(self.driver, 'captchaImg')
        expected = '账号不能为空'

        self.driver.implicitly_wait(10)

        # 输入用户名
        self.driver.find_element_by_name('user').send_keys(username)
        # 输入密码
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 验证码
        self.driver.find_element_by_name('captcha').send_keys(code)
        # 点击登录
        self.driver.find_element_by_class_name('btn-primary').click()

        # 等待提示框
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text == expected
        # self.assertEqual(alert.text, expected)
        alert.accept()
        time.sleep(3)

    # 测试后台登录，账号密码正确
    def test_admin_login_ok(self):
        username = 'liu'
        pwd = '13691959110'
        code = utils.get_code(self.driver, 'captchaImg')
        expected = 'JPress后台'

        # 输入用户名
        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(username)
        # 输入密码
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 验证码
        self.driver.find_element_by_name('captcha').clear()
        self.driver.find_element_by_name('captcha').send_keys(code)
        # 点击登录
        self.driver.find_element_by_class_name('btn-primary').click()

        # 等待提示框
        WebDriverWait(self.driver, 5).until(EC.title_is(expected))
        assert self.driver.title == expected
        # self.assertEqual(self.driver.title, expected)
        # self.driver.quit()

    # @classmethod
    def teardown_class(self):
        self.driver.quit()


if __name__ == '__main__':
    # loader = unittest.TestLoader()
    # suite = unittest.TestSuite()
    # suite.addTest(TestAdminLogin('test_admin_login_username_error'))
    # suite.addTest(TestAdminLogin('test_admin_login_ok'))
    # Testrunner = unittest.TextTestRunner()
    # Testrunner.run(suite)
    pytest.main(['test_admin_login.py'])
