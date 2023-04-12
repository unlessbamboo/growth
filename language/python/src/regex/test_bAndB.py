""" 测试单词边界特殊字符: \b, \B, 其他他们各自的含义如下:

\b: 表示字母数字与非字母数字的边界, 非字母数字与字母数字的边界
\B: 表示字母数字与(非非)字母数字的边界, 非字母数字与非字母数字的边界

参考: https://blog.csdn.net/uvyoaa/article/details/80854459
"""
import re


print('---------------1--------------')
ptn = r'123\b'
origin = '===123!! abc123. 123. 123abc. 123'
result = re.split(ptn, origin)
print(f'原始字符串: {origin}, 正则表达式: {ptn}, 进行分割之后的结果: {result}')
print()


print('---------------2--------------')
ptn = r'pyc\B'
origin = '1pycx223 py3 2pyc323 pyc1py2py4 pyp3 3pyc# pyc'
result = re.split(ptn, origin)
print(f'原始字符串: {origin}, 正则表达式: {ptn}, 进行分割之后的结果: {result}')
print()


print('---------------3--------------')
ptn = r'py=\B'
origin = '1py=x223 py3 2pyc323 pyc1py==py4 pyp3 3pyc# pyc'
result = re.split(ptn, origin)
print(f'原始字符串: {origin}, 正则表达式: {ptn}, 进行分割之后的结果: {result}')
print()
