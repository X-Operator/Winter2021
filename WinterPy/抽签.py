#！usr/bin/env python
# -*- coding:utf-8 -*-
import random
if __name__ == "__main__":
    boys = ['汪嘉俊','陈刘飞','冯松超','罗梓文','王云豪','何家铭','郑博中','郑兴春','胡平','刘清舟']
    girls = ['孔慧娴','魏维芮','蒋含颖','郭心怡','高洁','袁铨','王倩','赵甜','郭文青','吕嘉丽','席雯雯','刘育希','刘倩舒','程泽','张余珍','撖晓雨','李文涵']
    for i in range(10):
        thisgirl = random.randint(0,len(girls)-1)
        print(boys[i],girls[thisgirl])
        girls.remove(girls[thisgirl])
    for i in range(7):
        thisgirl = random.randint(0,len(girls)-1)
        b = random.randint(0,len(boys)-1)
        print(boys[b],girls[thisgirl])
        girls.remove(girls[thisgirl])
        boys.remove(boys[b])
    