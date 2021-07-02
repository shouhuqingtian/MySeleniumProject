# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class BaiduPage(object):
    def __init__(self):
        self.driver = webdriver.Firefox()

        self.input_element = (By.ID, 'kw')
        self.click_element = (By.ID, 'su')

    def goto_baidu(self, url):
        self.driver.get(url)

    def test_search(self, url, kw):
        self.goto_baidu(url)
        self.driver.find_element(*self.input_element).send_keys(kw)
        self.driver.find_element(*self.click_element).click()


class TestBaidu(unittest.TestCase):
    def setUp(self) -> None:
        self.baiduPage = BaiduPage()

    def test_search(self):
        self.baiduPage.test_search('https://www.baidu.com', 'selenium')


if __name__ == '__main__':
    unittest.main()
