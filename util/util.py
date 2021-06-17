# -*- coding:utf-8 -*-
import time
from util.untis import strtime, local_doc
from selenium import webdriver
from PIL import Image
import pytesseract


def get_code():  # 获取验证码照片
    driver = webdriver.Firefox()
    driver.get('http://www.jpress.io/user/register')
    # driver.get('https://kyfw.12306.cn/otn/resources/login.html')
    # driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
    driver.maximize_window()
    time.sleep(2)
    # 保存截图
    picture_name1 = local_doc() + '\screenshots/' + str(strtime()) + '.png'

    driver.save_screenshot(picture_name1)
    ce = driver.find_element_by_id('captchaimg')
    # ce = driver.find_element_by_xpath('//*[@id="J-loginImg"]')
    left = int(ce.location['x'])
    top = int(ce.location['y'])
    right = int(ce.size['width']) + left
    height = int(ce.size['height']) + top
    print(left, top, right, height, ce.location, ce.size)

    im = Image.open(picture_name1)
    img = im.crop((left, top, right, height))
    picture_name2 = local_doc() + '\screenshots/' + str(strtime()) + '.png'
    img.save(picture_name2)
    driver.quit()
