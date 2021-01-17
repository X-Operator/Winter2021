#！usr/bin/env python
# -*- coding:utf-8 -*-

import requests as rq
import re 

if __name__ == "__main__":
    url = input('请输入知乎网站的url:')
    headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }    
    page_text = rq.get(url=url,headers=headers).text
    ex = '<figure data-size="normal">.*?<img src="(.*?)" data.*?</figure>'
    img_list = re.findall(ex,page_text,re.S)
    index = 0
    for src in img_list:
        img_data = rq.get(url=src).content
        img_name = 'picture'+str(index)+'.jpg'
        index = index+1
        imgPath = './picture/'+img_name
        with open (imgPath,'wb') as f:
            f.write(img_data)
            print(img_name,'下载成功!')
    print('下载完毕!')
