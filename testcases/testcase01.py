# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep


def test02():
    driver = webdriver.Firefox()
    driver.get('http://www.jpress.io/user/register')


