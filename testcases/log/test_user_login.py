# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from util import utils


class TestUserLogin:
    # @classmethod
    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://159.75.96.188:18080/jpress/user/login')
        self.driver.maximize_window()
        self.logger = utils.get_logger()
        self.logger.info('测试用户登录')

    # 测试用户登录，用户名错误
    def test_user_login_username_error(self):
        # 用户名为空
        username = ''
        pwd = '123456'
        expected = '账号不能为空'

        # 输入用户名
        self.driver.find_element_by_name('user').send_keys(username)
        # self.logger.debug('输入用户名: %s', username)
        # 输入密码
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # self.logger.debug('输入密码: %s', pwd)
        # 点击登录
        self.driver.find_element_by_class_name('btn-primary').click()

        # 等待提示框
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text == expected
        # self.assertEqual(alert.text, expected)
        alert.accept()
        time.sleep(3)

    # 测试用户登录，账号密码正确
    def test_user_login_ok(self):
        # 用户名为空
        username = 'liu'
        pwd = '13691959110'
        expected = '用户中心'

        # 输入用户名
        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(username)
        # 输入密码
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 点击登录
        self.driver.find_element_by_class_name('btn-primary').click()

        # 等待提示框
        WebDriverWait(self.driver, 5).until(EC.title_is(expected))
        assert self.driver.title == expected
        # self.assertEqual(self.driver.title, expected)

    # @classmethod
    def teardown_class(self):
        self.driver.quit()


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # list = [TestUserLogin('test_user_login_username_error'), TestUserLogin('test_user_login_ok')]
    # suite.addTests(list)
    # unittest.TextTestRunner().run(suite)
    pytest.main(['-sv', 'test_user_login.py'])
