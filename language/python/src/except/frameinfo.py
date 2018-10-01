"""
利用inspect获取调用栈的详细信息, 一般用于调试
"""
from __func__ import print_function
import inspect


def hello():
    previous_frame = inspect.currentframe().f_back
    (filename, line_number,
     function_name, lines, index) = inspect.getframeinfo(previous_frame)
    return (filename, line_number, function_name, lines, index)


print((hello()))
