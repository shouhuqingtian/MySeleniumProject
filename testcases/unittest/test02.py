# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver


class MyTestCase02(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass...')
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://www.baidu.com')

    def test01(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        print('test01')

    def test02(self):
        print('test02')
        self.assertEqual('1, 1')
        self.assertIn(10, [1, 3, 4, 4])

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass...')
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main
