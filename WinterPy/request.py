#！usr/bin/env python
# -*- coding:utf-8 -*-

import requests as req

if __name__ == "__main__":
    # 指定url
    url='https://www.sogou.com/'
    response = req.get(url=url)
    page_text = response.text
    print(page_text)
    with open('sogou.html','w',encoding='utf-8') as f:
        f.write(page_text)
    

