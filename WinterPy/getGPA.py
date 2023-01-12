#！usr/bin/env python
# -*- coding:utf-8 -*-
import requests as rq
import re 
from selenium import webdriver
import time 
from lxml import etree
if __name__ == "__main__":
    print('这是自动计算GPA的程序:')
    username = input('请输入校园网账号(学号):')
    password = input('请输入校园网密码:')

    bro = webdriver.Safari()    #这里是用的Safari浏览器，可以换成别的，比如Chrome
    bro.get('http://info.tsinghua.edu.cn')
    #TODO:
    userName_tag = bro.find_element_by_id('userName')
    password_tag = bro.find_element_by_name('password')
    userName_tag.send_keys(username)
    password_tag.send_keys(password)
    btn = bro.find_element_by_class_name('but')
    btn.click()
    time.sleep(5)
    bro.execute_script("document.getElementsByTagName('a')[3].click();")
    time.sleep(3)
    bro.find_element_by_link_text("全部成绩").click()
    