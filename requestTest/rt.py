# -*- coding: UTF-8 -*-
# Time : 2023/1/18 12:58
# FILE : rt
# PROJECT : myProxyPool
# Author : kkk
import random

# 请求测试模块

import requests
# 导入测试url配置
from setting import setting


def requestTest(proxy):
    # 待测试代理
    proxys = {
        'http': f'{proxy}'
    }
    # 测试url
    testUrl = setting.testUrl[2]
    headers = setting.headers
    try:
        rep = requests.get(testUrl, headers=headers, proxies=proxys, timeout=2)
        if rep.status_code == 200:
            print(rep.text, proxy + '代理有效!')
            return True
        else:
            print(f"{proxy}代理无效!")
            return False
    except Exception as e:
        print(f"{proxy}代理无效!", e)
        return False
