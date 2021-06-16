# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import pyautogui


def test02():
    driver = webdriver.Firefox()
    driver.get('http://www.jpress.io/user/register')
    sleep(1)
    frame = driver.switch_to.frame(driver.find_element_by_xpath('/html/body/main/div/div/form/div[6]/div'))
    print(frame)
    element = driver.find_element_by_class_name('custom-control-input')
    element = element.rect
    print(element)
    pyautogui.click(element['x'], element['y'])
    # sleep(5)
    # driver.quit()


if __name__ == '__main__':
    test02()
