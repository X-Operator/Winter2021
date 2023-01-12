#！usr/bin/env python
# -*- coding:utf-8 -*-

import requests as rq
import re 
from bs4 import BeautifulSoup
from selenium import webdriver
import time 
import json
if __name__ == "__main__":

    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
    }               #UA伪装
    # username = input('请输入校园网账号(学号):')
    # password = input('请输入校园网密码:')
    username = '2019011159'
    password = 'thu200104250039'
    login_url = 'https://webvpn.tsinghua.edu.cn/do-login'
    data = {
        'auth_type': 'local',
        'username': username,
        'password': password,
        'captcha:':'',
        'needCaptcha':'false',
        'captcha_id': ''
    }
    sess = rq.Session()
    login = sess.post(url = login_url,headers = headers,data = json.dumps(data))
    login_page_text = login.text
    with open ('./test.html','w',encoding='utf-8') as f:
        f.write(login_page_text)
    info_url = 'http://info.tsinghua.edu.cn/out/help.jsp'
    print(login_page_text)
    # page_text = rq.get(url=info_url,headers=headers).text
    # print(page_text)
    # soup = BeautifulSoup(page_text,'lxml')
    # li_list = soup.select('.hot_nav > hot_nav_left > li')
    # print(li_list)
    
    