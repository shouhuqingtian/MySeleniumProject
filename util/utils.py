# -*- coding:utf-8 -*-
import random
import string

from util.unti_time import strtime, local_doc
from selenium import webdriver
from PIL import Image
from util.chaojiying import Chaojiying_Client


def get_code(driver, id):  # 获取验证码照片
    # 保存截图
    picture_name1 = local_doc() + '\screenshots/' + str(strtime()) + '.png'

    driver.save_screenshot(picture_name1)
    ce = driver.find_element_by_id(id)
    k = 1.25
    left = int(ce.location['x']*k)
    top = int(ce.location['y']*k)
    right = int(ce.size['width']*k) + left
    height = int(ce.size['height']*k) + top
    # 保存验证码图片
    im = Image.open(picture_name1)
    img = im.crop((left, top, right, height))
    picture_name2 = local_doc() + '\screenshots/' + str(strtime()) + '.png'
    img.save(picture_name2)
    chaojiying = Chaojiying_Client('shouhuqingtian', '13691959110', '96001')
    im = open(picture_name2, 'rb').read()
    code_value = chaojiying.PostPic(im, 1902)
    code = code_value['pic_str']
    return code


def gen_random_str():  # 随机生成字符串
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str
