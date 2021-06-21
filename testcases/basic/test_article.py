# -*- coding:utf-8 -*-
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestArticle(object):
    def __init__(self, login):
        self.login = login

    def test_add_ok(self):
        title = 'python入门到精通'
        content = 'Python 是一种解释型、面向对象、动态数据类型的高级程序设计语言。Python 由 Guido van Rossum 于 1989 年底发明，第一个公开发行版发行于 1991 年。像 Perl ' \
                  '语言一样, Python 源代码同样遵循 GPL(GNU General Public License) 协议。官方宣布，2020 年 1 月 1 日， 停止 Python 2 ' \
                  '的更新。Python 2.7 被确定为最后一个 Python 2.x 版本。 '
        expected = '文章保存成功。'
        self.login.driver.implicitly_wait(10)
        # 点击文章
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        # 点击写文章
        self.login.driver.find_element_by_link_text('写文章').click()
        # 写标题
        self.login.driver.find_element_by_id('article-title').send_keys(title)
        # 切换iFrame
        frame = self.login.driver.find_element_by_xpath('//iframe[@title="所见即所得编辑器, editor1"]')
        self.login.driver.switch_to.frame(frame)
        self.login.driver.find_element_by_xpath('/html/body').send_keys(content)
        # 切出iFrame
        self.login.driver.switch_to_default_content()
        # 点击发布
        self.login.driver.find_element_by_class_name('submitBtn').click()
        # 验证文章提示
        loc = (By.CLASS_NAME, 'toast-message')
        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))
        msg = self.login.driver.find_element(*loc).text
        assert msg == expected
        # 退出浏览器
        # self.login.driver.quit()

    def test_delete_one_article_ok(self):
        # 点击文章
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        # 点击文章管理
        self.login.driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[4]/ul/li[1]/a').click()

        link = self.login.driver.find_element_by_xpath('/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/strong/a')
        ActionChains(self.login.driver).move_to_element(link).perform()
        sleep(2)

        # 删除前文章数
        article_num = len(self.login.driver.find_elements_by_class_name('jp-actiontr'))
        self.login.driver.find_element_by_class_name('red-action').click()

        # 删除后文章数
        article_num_last = len(self.login.driver.find_elements_by_class_name('jp-actiontr'))
        # 判断文章数
        assert article_num == article_num_last + 1

    def test_delete_all_article_ok(self):
        # 点击文章
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        # 点击文章管理
        self.login.driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[4]/ul/li[1]/a').click()
        # 全选文章删除
        self.login.driver.find_element_by_xpath('//input[@type="checkbox"]').click()
        self.login.driver.find_element_by_id('batchDel').click()
        # 弹窗选择是
        self.login.driver.switch_to.alert.accept()



