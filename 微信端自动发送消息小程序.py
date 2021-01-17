#！usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests


bot = Bot()

def get_news():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation= r.json()['note']
    print(contents,translation)
    return contents,translation

def send_news():
    try:
        friendname = input('请输入你朋友的微信名称，不是备注，也不是微信帐号:')
        my_friend = bot.friends().search(friendname)[0]    #你朋友的微信名称，不是备注，也不是微信帐号。
        my_friend.send(get_news1()[0])
        my_friend.send(get_news1()[1][5:])
        my_friend.send(u"每日一句！")
        t = Timer(20, send_news)
        t.start()
    except:
        myname = input ('请输入你的微信名称，不是备注，也不是微信帐号:')#你的微信名称，不是备注，也不是微信帐号。
        my_friend = bot.friends().search(myname)[0]
        my_friend.send(u"今天消息发送失败了")

if __name__ == "__main__":
    send_news()
    
