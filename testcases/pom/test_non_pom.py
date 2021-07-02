# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest


class TestBaidu(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://www.baidu.com')

    def test_baidu(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()

    def tearDown(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
