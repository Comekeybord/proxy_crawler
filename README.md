# proxy_crawler使用文档

# 一、版权声明

1. 开源声明：

- MIT License
  MIT License
  MIT是和BSD一样宽范的许可协议,作者只想保留版权,而无任何其他了限制.也就是说,你必须在你的发行版里包含原许可协议的声明,无论你是以二进制发布的还是以源代码发布的.总结一下只有三段话，允许任何人进行个人使用、商业使用、复制、分发、修改，唯一的限制就是，必须得加上源码作者的版权信息（CopyRight）是一个相对宽松的常用的协议

2. 本协议采用的开源协议

- MIT License

# 二、项目依赖

1. 配置依赖  
   在项目目录下运行命令 `pip install -r requirements.txt`
   安装好项目所用到的依赖
2. 数据库配置
   本项目采用 `MySql` 数据库，首先自己
   建一个数据库和表然后在 `setting.py` 文件
   中进行配置
3. 具体细节在 `setting.py` 配置文件中已写

# 三、项目所用资源

1. 项目爬取所用的免费代理网站
    <table style="text-align:center">
    <thead>
    <tr>
        <td>网站名称</td>
        <td>网站地址</td>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>66免费代理网</td>
    <td>
        <a href="http://www.66ip.cn/">66免费代理网</a>
    </td>
    </tr>
    <tr>
    <td>fatezero</td>
    <td>
        <a href="http://proxylist.fatezero.org/">fatezero</a>
    </td>
    </tr>
    <tr>
    <td>云代理</td>
    <td>
        <a href="http://www.ip3366.net/">云代理</a>
    </td>
    </tr>
    </tbody>
    </table>

# 四、使用方式

1. 配置好 `setting.py` 文件与数据库
2. 直接运行 `run.py` 文件

# 五、项目作者

1. github主页  
   [Comekeybord](https://github.com/Comekeybord)