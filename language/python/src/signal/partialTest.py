""" 偏函数使用
@javascript: 偏函数有点类似js的bind方法
    function f1 (num1, num2, num3) {
        return num1 + num2 + num3
    }
    console.log(f1(1, 2, 3));
    var f2 = f1.bind(this, 1, 2);
    console.log(f2(3));
"""
from functools import partial
from datetime import datetime, timedelta


def get_next_day(baseday, n=1):
    """ 获取下一天日期信息

    :param baseday: 当前日期, 格式: YYYY-mm-dd
    :param n: 增加日期数, 默认为1
    """
    return (datetime.strptime(str(baseday), '%Y-%m-%d') + timedelta(days=n)).date()


nday = partial(get_next_day, '2015-01-01')
print(nday(1))
print(nday(3))
