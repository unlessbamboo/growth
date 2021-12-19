""" python测试代码的通用工具函数 """
import sys
import inspect
from functools import wraps


execute_num = 0


def show_function(desc=None):
    """ 执行装饰函数, 打印整个函数体

    :param desc: 函数功能描述
    """

    def wrap(func):
        @wraps(func)
        def _wrap(*args, **kwargs):
            func_desc = desc if desc else '未知描述'

            global execute_num  # pylint: disable=global-statement

            execute_num += 1
            module = sys.modules[func.__module__]
            print(f'\033[32m-----------{func_desc}-----------\033[0m')
            print(f'\033[32m模块:{module}\033[0m\n')
            print(f'\033[31m{inspect.getsource(func)}\033[0m')
            print(f'> \033[32m函数执行结果(当前执行顺序{execute_num}):\033[0m\n')
            try:
                value = func(*args, **kwargs)
                if inspect.isfunction(value):
                    value()
            except Exception as msg:
                print(f'函数执行发生异常:{msg}')
            finally:
                print('\033[32m-------------------end-----------------\033[0m\n\n')
        return _wrap

    return wrap
