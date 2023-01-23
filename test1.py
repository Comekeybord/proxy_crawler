# -*- coding: UTF-8 -*-
# Time : 2023/1/24 0:11
# FILE : test1.py
# PROJECT : proxy_crawler
# Author : kkk

import requests
from setting import setting


def requestTest(proxy):
    # 待测试代理
    proxys = {
        'http': f'{proxy}'
    }
    # 测试url
    testUrl = setting.testUrl[1]
    headers = setting.headers
    try:
        # 设置重连次数
        requests.adapters.DEFAULT_RETRIES = 3
        rep = requests.get(testUrl, headers=headers, proxies=proxys)
        # if rep.status_code == 200:
        #     # print(rep)
        #     return True
        # else:
        #     return False
        # 检测方式二：通过外部站点检测，若有效则会返回ip本身
        proxyIP = rep.text
        print(proxyIP)
        if proxyIP == proxy:
            print("代理IP:'" + proxyIP + "'有效！")
            return True
        else:
            print("2代理IP无效！")
            return False
    except Exception as e:
        # print(e)
        print("1代理IP无效！", e)
        return False


requestTest('60.211.218.78:53281')
