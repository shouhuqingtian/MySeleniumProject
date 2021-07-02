# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium import webdriver


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, *args):
        return self.driver.find_element(*args)

    def input_text(self, text, *args):
        return self.driver.find_element(*args).send_keys(text)

    def click(self, *args):
        return self.driver.find_element(*args).click()

    def get_title(self):
        return self.driver.title


class BaiduPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # BasePage.__init__(self, driver)
        driver.get('https://www.baidu.com')

    def test_search(self):
        loc = (By.ID, 'kw')
        loc2 = (By.ID, 'su')
        self.input_text('text', *loc)
        self.click(*loc2)


if __name__ == '__main__':
    drive = webdriver.Firefox()
    run = BaiduPage(drive)
    run.test_search()
    print(BaiduPage.__bases__)
