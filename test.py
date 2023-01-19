# -*- coding: UTF-8 -*-
# Time : 2023/1/17 21:40
# FILE : test
# PROJECT : myProxyPool
# Author : kkk
import random

import requests
import json
import re
from lxml import etree

url = 'http://www.ip3366.net/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv': '106.0) Gecko/20100101 Firefox/106.0",
}

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
]
headers['User-Agent'] = random.choice(user_agent_list)

# ip3366代理网站爬取测试
xpath = [
    '//table//tr//td[1]/text()',
    '//table//tr//td[2]/text()'
]

content = requests.get(url, headers=headers).text
tree = etree.HTML(content)
ipList = tree.xpath(xpath[0])
portList = tree.xpath(xpath[1])
print(len(ipList), '\n', len(portList))
for i in range(5):
    print(i)

# 抓包看一下问题
# proxy = {
#     'http': '127.0.0.1:33210'
# }

# xpath = [
#     '//table//tr//td[1]/text()',
#     '//table//tr//td[2]/text()'
# ]
# try:

# try:
#     content = requests.get(url, headers, timeout=2)
#     print('success')
# except requests.exceptions.RequestException as e:
#     print(e)


# # 利用正则表达式过滤出ip与端口
# ipPattern = re.compile('\d+.\d+.\d+.\d+')
# portPattern = re.compile('port": \d{4}')
# ipList = ipPattern.findall(content)
# portTemp = portPattern.findall(content)
# portList = []
# # 再次过滤portTemp
# for item in portTemp:
#     portList.append(re.findall('\d+', item)[0])
#
# res = {}
# if len(portList) > len(ipList):
#     length = len(ipList)
# else:
#     length = len(portList)
#
# for i in range(length):
#     res[ipList[i]] = portList[i]
# print(res)
