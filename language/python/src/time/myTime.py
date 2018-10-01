# coding:utf8
"""
    所有时间操作集合
    pytz文档: http://pytz.sourceforge.net/
"""
import time
from datetime import datetime, timedelta, date
import pytz
from dateutil import parser
from dateutil.relativedelta import relativedelta


FMT = '%Y-%m-%d %H:%M:%S %Z%z'


def country_timezones_by_code(country_code):
    """根据国家码获取所有的时区"""
    return pytz.country_timezones[country_code.upper()]


def datetime_to_timezone(dt, tz=None):
    """
    将datetime转换为timezone, 默认情况下, datetime没有timezone信息
    """
    # 返回tzinfo实例对象
    local = pytz.timezone(tz) if tz else pytz.timezone('Asia/Shanghai')

    # 方法1: localize--对datetime操作, 其中is_dst表示夏令时
    local_tz = local.localize(dt, is_dst=False)

    # 方法2: astimezone--对timezone操作, 转换为其他时区
    local_tz = local_tz.astimezone(local)

    return local_tz


def timestamp_to_utc(timestamp):
    """将timestamp转为utc timezone时间"""
    utc_dt = datetime.utcfromtimestamp(timestamp)
    return pytz.UTC.localize(utc_dt)


def time_after_or_before_as_type(today=None, interval=0, types='days'):
    """获取以today为基准的前后日期时间值, today如果为空, 则默认为当天"""
    if types == 'years':
        today = datetime.now() if not today else today
        today = today + relativedelta(years=interval) if interval else today
    elif types == 'months':
        today = datetime.now() if not today else today
        today = today + relativedelta(months=interval) if interval else today
    elif types == 'days':
        # 今天, 前天, 前前天, 明天, ...
        today = date.today() if not today else today
        # 其实可以使用relativedelta来完成
        today = today + timedelta(days=interval) if interval else today
    elif types == 'weeks':
        # 这个礼拜, 下个礼拜, 获取礼拜几信息: today.weekday()
        today = date.today() if not today else today
        today = today + timedelta(weeks=interval) if interval else today
    elif types == 'hours':
        today = datetime.now() if not today else today
        today = today + timedelta(hours=interval) if interval else today
    elif types == 'minutes':
        today = datetime.now() if not today else today
        today = today + timedelta(minutes=interval) if interval else today

    return today


def timestr_to_timestamp(times, formats):
    """
    Formats: %Y%m%d or %Y-%m-%d %H:%M:%S or other
    """
    # str -> local datetime, 默认情况下, datetime没有timezone信息
    dt = datetime.strptime(times, formats)
    timetuple = dt.timetuple()
    return int(time.mktime(timetuple))


def timezone_to_daylight_timezone(timezone, dt):
    """转换为夏时制
    timezone: 时区信息
    dt: timezone格式的datetime时间
    """
    return timezone.normalize(dt).strftime(FMT)


def timezone_to_fake_timezone(timezone, tz=0):
    """
    功能: 在大部分情况下, 无法提供timezone信息, 但是仅仅存在tz.
    注意: 这种特殊情况下无法保存数据库, 因为时区会被重置为 UTC, 仅仅为为了获取month
    """
    assert -24 <= tz <= 24
    # change timezone
    utc_tz = timezone.astimezone(pytz.UTC)
    # timedelta: days, hours, minutes, weeks, seconds, miliseconds
    # relativedelta: years, months, days, hours, minutes, microseconds
    utc_tz = utc_tz + timedelta(hours=tz)
    return utc_tz


def first_day_after_or_before_as_type(today=None, interval=0, types='months'):
    """获取today所在的下一个季度的第一天"""
    today = datetime.now() if not today else today
    result = today

    if types == 'quarters':
        quarter = ((today.month - 1) // 3 + interval) * 3 + 1
        quarter_months = quarter - today.month

        result = today + relativedelta(months=quarter_months)
        result = result - relativedelta(days=today.day - 1)
    elif types == 'months':
        today = today + relativedelta(months=interval) if interval else today
        result = today.replace(day=1)
    elif types == 'years':
        today = today + relativedelta(years=interval) if interval else today
        result = replace(month=1, day=1)

    return result


if __name__ == '__main__':
    # 1 测试时间字符串转timestamp
    print('时间201701转换为timestamp: ', timestr_to_timestamp('201701', '%Y%m'))

    # 2 将本地时区转换为特定的时区值
    now = parser.parse('2017-01-03 18:00:00')
    now_tz = datetime_to_timezone(now)
    timezone_9_tz = timezone_to_fake_timezone(now_tz, 9)
    print('第8时区的时间值:', now_tz)
    print('第9时区的时间值(伪):', timezone_9_tz)

    # 3 将timestamp转为utc timezone
    timestamp = 1143408899
    print('转换timestamp:{} to utc:{}'.format(
        timestamp, timestamp_to_utc(timestamp)))

    # 4 获取某一个国家的所有timezone信息
    print('国家码: CN, 拥有的时区:', country_timezones_by_code('cn'))

    # 5 获取某一个日期之后的天数
    print('今天:', time_after_or_before_as_type(types='days'))
    print('后天:', time_after_or_before_as_type(types='days', interval=2))
    print('今年:', time_after_or_before_as_type(types='years').year)
    print('5年后:', time_after_or_before_as_type(types='years', interval=5).year)
    print('下周:', time_after_or_before_as_type(types='weeks', interval=1))
    now = datetime.now()
    print('下下周:', time_after_or_before_as_type(
        types='weeks', interval=2, today=now))

    # 6 下一个季度
    print('当前季度第一天:', first_day_after_or_before_as_type(now, types='quarters'))
    print('下二个季度第一天:', first_day_after_or_before_as_type(
        now, types='quarters', interval=2))
    print('上一个季度第一天:', first_day_after_or_before_as_type(
        now, types='quarters', interval=-1))
    print('上三个季度第一天:', first_day_after_or_before_as_type(
        now, types='quarters', interval=-3))
