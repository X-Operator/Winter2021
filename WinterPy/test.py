#！usr/bin/env python
# -*- coding:utf-8 -*-

import requests as rq
import re 
from selenium import webdriver
import time 
from lxml import etree
if __name__ == "__main__":
    password = 'thu200104250039'
    ts = "password=document.getElementsByName('password');password.values ='thu200104250039'"
    ts2 = "password=document.getElementsByName('password');password.values =%s"%password
    print(ts)
    print(ts2)
