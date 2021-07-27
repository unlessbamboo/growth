
def seconds_format(time_cost: int):
    """
    耗费时间格式转换
    :param time_cost: 
    :return: 
    """
    min = 60
    hour = 60 * 60
    day = 60 * 60 * 24
    if not time_cost or time_cost < 0:
        return '0秒'
    elif time_cost < min:
        return '%s秒' % time_cost
    elif time_cost < hour:
        return '%s分%s秒' % (divmod(time_cost, min))
    elif time_cost < day:
        cost_hour, cost_min = divmod(time_cost, hour)
        if cost_min > min:
            return '%s时%s' % (cost_hour, seconds_format(cost_min))
        else:
            return '%s时0分%s' % (cost_hour, seconds_format(cost_min))
    else:
        cost_day, cost_hour = divmod(time_cost, day)
        if cost_hour >= hour:
            return '%s天%s' % (cost_day, seconds_format(cost_hour))
        elif cost_hour >= min:
            return '%s天0时%s' % (cost_day, seconds_format(cost_hour))
        else:
            return '%s天0时0分%s' % (cost_day, seconds_format(cost_hour))


if __name__ == '__main__':
	print(seconds_format(1))
	print(seconds_format(393993))
	print(seconds_format(0))
	print(seconds_format(60))
	print(seconds_format(3600))
