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
    testUrl = setting.testUrl[0]
    headers = setting.headers
    try:
        if requests.get(testUrl, headers=headers, proxies=proxys, timeout=2):
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        # print(e)
        return False
