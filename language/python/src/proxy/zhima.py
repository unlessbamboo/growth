# coding:utf8
"""
芝麻代理:  调用芝麻代理接口, 获取IP信息
"""
import requests

# 请求地址
targetUrl = "http://baidu.com"

# 代理服务器
proxyHost = "36.32.44.50"
proxyPort = "6436"

proxyMeta = "http://%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
}


proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

for _ in range(25):
    resp = requests.get(targetUrl, proxies=proxies)
    print(resp.status_code)
    print(resp.text)
