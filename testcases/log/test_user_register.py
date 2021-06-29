# -*- coding:utf-8 -*-
import logging
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import utils
import pytest


class TestUserRegister:
    # @classmethod
    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://159.75.96.188:18080/jpress/user/register')
        self.driver.maximize_window()
        self.logger = utils.get_logger()
        logging.info('测试用户注册')
        time.sleep(1)

    # 测试登录验证码错误
    def test_register_code_error(self):
        username = 'test001'
        email = 'test001@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        captcha = '666'
        expected = '验证码不正确'

        self.driver.find_element_by_name('username').send_keys(username)
        self.logger.debug('输入用户名： %s', username)
        self.driver.find_element_by_name('email').send_keys(email)
        self.logger.debug('输入邮箱： %s', email)

        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.logger.debug('输入密码： %s', pwd)
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
        self.logger.debug('确认密码： %s', confirmPwd)
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.logger.debug('输入验证码： %s', captcha)
        self.driver.find_element_by_class_name('btn-primary').click()
        self.logger.debug('点击登录')

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # python断言
        try:
            assert alert.text == expected
        except AssertionError as ae:
            self.logger.error('报错了, 宝')
        # self.assertEqual(alert.text, expected, '登录验证码断言失败')
        alert.accept()
        sleep(3)

    def test_register_ok(self):
        username = utils.gen_random_str()
        email = username + '@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        expected = '注册成功，点击确定进行登录。'

        # 输入用户名
        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys(username)
        self.logger.debug('输入用户名： %s', username)
        # email
        self.driver.find_element_by_name('email').clear()
        self.driver.find_element_by_name('email').send_keys(email)
        self.logger.debug('输入邮箱： %s', email)

        # 密码
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.logger.debug('输入密码： %s', pwd)

        # 确认密码
        self.driver.find_element_by_name('confirmPwd').clear()
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
        self.logger.debug('确认密码： %s', confirmPwd)

        # 自动识别验证码
        self.driver.find_element_by_name('captcha').clear()
        captcha = utils.get_code(self.driver, 'captchaimg')
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.logger.debug('输入用户名： %s', captcha)
        self.driver.find_element_by_class_name('btn-primary').click()
        self.logger.debug('点击登录 %s')
        # 等待alert出现
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # 验证
        try:
            assert alert.text == expected + str(2)
        except AssertionError as ae:
            self.logger.error('出错了， 宝')
        # self.assertEqual(alert.text, expected, '登录断言失败')
        alert.accept()
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['test_user_register.py'])
