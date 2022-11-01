""" 命名空间说明 """
from util import show_function  # pylint: disable=import-error
import os
import sys

COMMON_PATH = os.path.abspath(os.path.dirname(
    os.path.dirname(__file__))) + os.sep + 'common'
sys.path.insert(0, COMMON_PATH)

# 1. 打印内建命名空间信息
print(f'内建命名空间信息:{dir(__builtins__)}')


# 2. 简单的命名空间
@show_function(desc='命名空间-简单定义')
def ns_local():
    global h  # 注意, 这里不能用nonlocal, 除非再嵌套一层
    x, y, z = 1, {}, 'wa'  # pylint: disable=possibly-unused-variable
    h = h + 1  # pylint: disable=used-before-assignment
    print(f'局部命名空间中的值:{locals()}, h值: {h}')


x, y, h = 2, [], -2
ns_local()
ns_local()
ns_local()
print(f'全局命名空间中的值:{globals()}')
