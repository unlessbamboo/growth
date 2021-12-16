""" python测试代码的通用工具函数 """
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
            print(f'-----------{func_desc}-----------')
            print(inspect.getsource(func))
            print(f'> 函数执行结果(当前执行顺序{execute_num}):\n')
            try:
                value = func(*args, **kwargs)
                if inspect.isfunction(value):
                    value()
            except Exception as msg:
                print(f'函数执行发生异常:{msg}')
            finally:
                print('-----------end-----------\n\n')
        return _wrap

    return wrap
