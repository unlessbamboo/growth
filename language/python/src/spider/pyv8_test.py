# coding:utf8
"""
PyV8在爬虫中的使用
"""
from __future__ import print_function
import os
import sys
import re
import requests
try:
    import PyV8
except Exception:
    _my_pyv8_path = os.path.expanduser('~/Software/v8/pyv8-osx-p3/')
    sys.path.append(_my_pyv8_path)
    import PyV8


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def get_kuaidaili_html(url, cookie=None):
    header = {
        "Host": "www.kuaidaili.com",
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }
    rsp = requests.get(url=url, headers=header, timeout=60, cookies=cookie)
    if rsp.status_code != 200:
        print('获取页面:{}失败, code:{}'.format(url, rsp.status_code))
        return None
    return rsp.content


def test_kuaidaili():
    """对快代理上cookie加密的解决办法
    @refer: https://zhuanlan.zhihu.com/p/25957793
    """
    kuai_url = "http://www.kuaidaili.com/proxylist/1/"
    # 首次访问获取动态加密的JS
    kuai_first_html = get_kuaidaili_html(kuai_url)
    if not kuai_first_html:
        return False
    # 执行js代码, 获取cookies信息
    ctxt = PyV8.JSContext()
    ctxt.__enter__()
    js_path = BASE_DIR + os.sep + 'hm.js'
    js_data = None
    with open(js_path, 'r') as fd:
        js_data = fd.read()
    if not js_data:
        print('读取的hm.js文本为空')
        return False
    js_data_html = """
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <script type="text/javascript">
        {}
        </script>
    </head>
</html>
    """.format(js_data)
    import pdb
    pdb.set_trace()
    ctxt.eval(js_data)
    print('Success execute javascript code')


if __name__ == '__main__':
    """使用pyv8执行kuaidaili上的某一个生成cookie的js文件, 以进行后续的数据爬取"""
    test_kuaidaili()
