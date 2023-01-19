# -*- coding: UTF-8 -*-
# Time : 2023/1/15 21:45
# FILE : spider.py
# PROJECT : myProxyPool
# Author : kkk

# 导入requests
import requests
# 导入线程操作对象
import threading
# 导入xpath
from lxml import etree
# 导入配置文件
from setting import setting
# 导入队列queue 线程的执行结果，无法通过return进行返回，使用Queue存储
from queue import Queue
# 导入正则表达式模块
import re


# 爬取每个接口的十个免费代理
def spidePage1(url, xpath, q):
    text = requests.get(url, setting.headers).text
    # print(type(text))
    # 通过xpath过滤内容
    # print(text)
    tree = etree.HTML(text)
    res = {}
    ipList = tree.xpath(xpath[0])
    portList = tree.xpath(xpath[1])
    for i in range(1, len(ipList)):
        res[ipList[i]] = portList[i]
    q.put(res)


def spidePage2(url, q, proxy=None):
    if proxy:
        content = requests.get(url, setting.headers, proxies=proxy).text
    else:
        content = requests.get(url, setting.headers).text
    # 利用正则表达式过滤出ip与端口
    ipPattern = re.compile('\d+.\d+.\d+.\d+')
    portPattern = re.compile('port": \d{4}')
    ipList = ipPattern.findall(content)
    portTemp = portPattern.findall(content)
    portList = []
    # 再次过滤portTemp
    for item in portTemp:
        portList.append(re.findall('\d+', item)[0])
    res = {}
    if len(portList) > len(ipList):
        length = len(ipList)
    else:
        length = len(portList)

    for i in range(length):
        res[ipList[i]] = portList[i]
    q.put(res)


def spidePage3(url, xpath, q):
    content = requests.get(url, headers=setting.headers).text
    tree = etree.HTML(content)
    res = {}
    ipList = tree.xpath(xpath[0])
    portList = tree.xpath(xpath[1])
    for i in range(0, len(ipList)):
        res[ipList[i]] = portList[i]
    q.put(res)


def spideStart():
    print('开始爬行...')
    # 创建队列
    q = Queue()
    # 创建几个线程
    threads = []
    t1 = threading.Thread(target=spidePage1, args=(setting.url[0], setting.xpath[0], q))
    t2 = threading.Thread(target=spidePage2, args=(setting.url[1], q, setting.proxy))
    t3 = threading.Thread(target=spidePage3, args=(setting.url[2], setting.xpath[2], q))
    # 添加到线程列表
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    for thread in threads:
        # 开始线程
        thread.start()
        # 阻塞线程
        thread.join()
    resultsTemp = []
    for i in range(setting.threadNumber):
        resultsTemp.append(q.get())

    # 导入代理测试模块
    from requestTest import rt
    # 导入数据库操作
    from database import db
    # 将结果存入数据库
    print('测试代理并存储到数据库...')
    for res in resultsTemp:
        for key in res:
            ip = str(key)
            port = int(res[key])
            proxy = f"{ip}:{port}"
            if rt.requestTest(proxy):
                db.insertData(ip, port, 1)
    try:
        # 提交修改
        db.db.commit()
        # 关闭游标
        db.cur.close()
        # 关闭数据库
        db.db.close()
        print('数据库操作提交成功!')
    except Exception as e:
        print('数据库操作提交失败!', e)
