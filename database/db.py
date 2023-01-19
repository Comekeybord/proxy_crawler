# -*- coding: UTF-8 -*-
# Time : 2023/1/15 14:20
# FILE : db.py
# PROJECT : myProxyPool
# Author : kkk
# 数据库链接文件

# 导入数据库操作库
import pymysql

# 导入数据库配置
from setting.setting import dbSetting

# 创建数据库链接
db = pymysql.connect(
    host=dbSetting['host'],
    port=dbSetting['port'],
    user=dbSetting['usr'],
    password=dbSetting['pwd'],
    charset='utf8',
    database=dbSetting['dbName'],
)
print('数据库链接成功!')

# 创建游标对象cursor（操作数据库的对象）
cur = db.cursor()


# 执行数据库操作函数
def commit(sql):
    try:
        # print(cur)
        # 使用 execute()  方法执行 SQL 语句
        cur.execute(sql)
        return cur.fetchall()
    except Exception as e:
        print('数据库操作错误!', e)


# 插入数据函数
def insertData(ip, port, live):
    # 定义sql语句
    # ip是字符类型，port是int型，live是tinyint类型
    sql = '''
    insert into {} (proxy_ip,proxy_port,is_live) values ('{}',{},{})
    '''.format(dbSetting['tableName'], ip, port, live)
    commit(sql)


# 查询数据函数
def selectData(ip):
    # 定义sql语句
    sql = '''
    select * from proxy_list where proxy_ip='{}'
    '''.format(ip)
    return commit(sql)

# insertData('192.168.0.33', 888, 1)