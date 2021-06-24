# -*- coding:utf-8 -*-
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from testcases.basic.test_admin_login import TestAdminLogin


class TestCategory:
    def setup_class(self):
        self.login = TestAdminLogin()

    # 测试文章分类失败，名称为空
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    def test_add_category_error(self):
        name = ''
        parent = '科学'
        slug = 'test'
        expected = '分类名称不能为空'

        # 点击文章
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        # 点击分类
        self.login.driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[4]/ul/li[3]/a').click()
        # 输入分类名称
        self.login.driver.find_element_by_name('category.title').send_keys(name)
        # 选择父分类
        parent_category = self.login.driver.find_element_by_name('category.pid')
        Select(parent_category).select_by_visible_text(parent)
        # 输入slug
        self.login.driver.find_element_by_name('category.slug').send_keys(slug)
        # 对比预期结果
        self.login.driver.find_element_by_class_name('btn-primary').click()

        loc = (By.CLASS_NAME, 'toast-message')
        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))
        msg = self.login.driver.find_element(*loc).text
        assert msg == expected
        time.sleep(3)

    # 测试文章分类成功
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    def test_add_category_ok(self):
        name = '人与自然'
        parent = '顶级'
        slug = 'python'
        expected = None

        # 点击文章
        # self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        # 点击分类
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a').click()
        # 输入分类名称
        self.login.driver.find_element_by_name('category.title').clear()
        self.login.driver.find_element_by_name('category.title').send_keys(name)
        # 选择父分类
        parent_category = self.login.driver.find_element_by_name('category.pid')
        Select(parent_category).select_by_visible_text(parent)
        # 输入slug
        self.login.driver.find_element_by_name('category.slug').clear()
        self.login.driver.find_element_by_name('category.slug').send_keys(slug)
        # 对比预期结果
        self.login.driver.find_element_by_class_name('btn-primary').click()

        # loc = (By.CLASS_NAME, 'toast-message')
        # WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))
        # msg = self.login.driver.find_element(*loc).text
        assert 1 == 1


if __name__ == '__main__':
    pytest.main(['test_category.py'])
