#！usr/bin/env python
# -*- coding:utf-8 -*-

import requests as req

if __name__ == "__main__":
    headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15'
    }
    url='https://www.sogou.com/web'
    kw = input('enter a word:')
    param = {
        'query':kw
    }
    response = req.get(url=url,params=param,headers=headers)
    page_text = response.text
    fileName = kw+'.html'
    with open (fileName,'w',encoding='utf-8') as f:
        f.write(page_text)
    print(fileName,'保存成功!')
