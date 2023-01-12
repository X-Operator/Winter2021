#！usr/bin/env python
# -*- coding:utf-8 -*-

import requests as re

if __name__ == "__main__":
    url = 'http://i1.shaodiyejin.com/uploads/tu/201908/9999/2d40e22474.jpg'
    img_data = re.get(url=url).content
    with open('girl.jpg','wb') as f:
        f.write(img_data)