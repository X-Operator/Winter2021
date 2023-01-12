#！usr/bin/env python
# -*- coding:utf-8 -*-

import requests as re
import json
if __name__ == "__main__":
    post_url = 'https://www.baidu.com/sug'
    headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15'
    }
    word =input('enter a word:')
    data = {
        'kw': word
    }

    response = re.post(url=post_url,data=data,headers=headers)
    dic_obj = response.json()
    # print(dic_obj)
    fname = word + '.json'
    fp = open(fname,'w',encoding= 'utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)

