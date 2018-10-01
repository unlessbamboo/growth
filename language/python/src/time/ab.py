# coding:utf8
"""
进行ab测试, 获取不同并发数情况下某一个特定接口RPS值;
其中HTTP服务由UWSGI启动;
"""

import re
import os


match_tpr = re.compile(r'Requests per second:[ ]*?(\d+\.?\d*?) \[#/sec\] \(mean\)')
header = 'application/json'
url = 'http://127.0.0.1:5000/api/v2/evisa/sign'
totals = 2000
json_file = './tests/ab/evisa_sign.json'

print('----begin-----')
for cnum in (5, 10, 15, 20):
    result = os.popen("ab -c {} -n {} -p {} -T '{}' {} 2> /dev/null".format(
        cnum, totals, json_file, header, url)).read()
    match = match_tpr.search(result)
    if match:
        rps = match.groups()[0]
        print('Total Requests: {} Concurrency: {} Qps: {}'.format(totals, cnum, rps))
    else:
        print('Not found Request Per Second value....')

print('----end-----')
