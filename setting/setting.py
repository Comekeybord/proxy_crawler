# -*- coding: UTF-8 -*-
# Time : 2023/1/15 21:48
# FILE : setting
# PROJECT : myProxyPool
# Author : kkk


# 配置文件


# 注意：数据库自己先创建好
# 数据库配置
dbSetting = {
    'host': 'localhost',
    'port': 3306,
    'usr': 'root',
    'pwd': 'admin666',
    'dbName': 'proxy_pool',
    'tableName': 'proxy_list',
}

# 线程配置
# 线程数要与爬取的网站数相同,否则无法运行
threadNumber = 3

# 第二个网站需要科学上网才能爬取
# 通过科学上网代理爬取
# 如果没有科学上网代理就到spider模块中把第二个线程注释了
proxy = {
    'http': '127.0.0.1:33210'
}
# 从以下代理网站爬取
url = [
    'http://www.66ip.cn/',
    'http://proxylist.fatezero.org/proxy.list',
    'http://www.ip3366.net/'
]

# 对应xpath配置
xpath = [
    ['//div[@id="main"]//div[@align="center"]/table//tr/td[1]/text()',
     '//div[@id="main"]//div[@align="center"]/table//tr/td[2]/text()'
     ],
    [],  # 占位
    [
        '//table//tr//td[1]/text()',
        '//table//tr//td[2]/text()'
    ]
]

# 定制头部
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
}

# 测试代理所用的网址
testUrl = [
    'https://www.baidu.com/',
]
