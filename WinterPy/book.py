#！usr/bin/env python
# -*- coding:utf-8 -*-

import requests as rq
import re 
from bs4 import BeautifulSoup
import time
if __name__ == "__main__":
    # 爬取古诗文网的书籍内容
    # 找到首页的页面数据
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
    }
    url = 'https://www.shicimingju.com/book/xintangshu.html' 
    page_text = rq.get(url=url,headers=headers).text
    # 解析标题和详情页的url
    # 1.实例化BeautifulSoup对象
    soup = BeautifulSoup(page_text,'lxml')
    # 解析章节标题和详情页的url
    #需要根据实际情况调整
    li_list = soup.select('.book-mulu > ul > li')
    f = open('./picture/新唐书.txt','w',encoding='utf-8')
    for li in li_list:
        if li.a:
            title = li.a.string
            detail_url = 'https://www.shicimingju.com' + li.a['href']
            # 对详情页发起请求，解析章节的内容
            detail_page_text = rq.get(url=detail_url,headers=headers).text
            detail_soup = BeautifulSoup(detail_page_text,'lxml')
            every_text = detail_soup.find('div',class_='chapter_content')
            content = every_text.text
            f.write(title+':'+content+'\n')
            print(title,'爬取成功！')
            time.sleep(0.1)
    print('爬取完毕！')


