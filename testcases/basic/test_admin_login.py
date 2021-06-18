# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.utils import get_code

class TestAdminLogin(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://159.75.96.188:18080/jpress/admin/login')
        self.driver.maximize_window()

    # 测试后台登录，用户名错误
    def test_admin_login_username_error(self):
        # 用户名为空
        username = ''
        pwd = '123456'
        code = get_code(self.driver, 'captchaImg')
        expected = '账号不能为空'

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
        alert.accept()
        time.sleep(3)

    # 测试后台登录，账号密码正确
    def test_admin_login_ok(self):
        username = 'liu'
        pwd = '13691959110'
        code = get_code(self.driver, 'captchaImg')
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
        # self.driver.quit()
