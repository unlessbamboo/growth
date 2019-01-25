#!/usr/bin/env python
# coding:utf8
"""
解析时间文件
"""
import json
import datetime
import glob
import numpy as np
import matplotlib.pyplot as plt

from dateutil.relativedelta import relativedelta


# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
# 显示正负号
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['savefig.dpi'] = 300  # 图片像素


def parse():
    """ 解析当前目录下所有数据并构建为符合要求的数据, 以便生成matloplib图片 """
    def parse_and_save(filename, new_filename):
        data = {}
        with open(filename, 'r') as fd:
            lines = fd.readlines(100000)
            for line in lines:
                lineprefix, times = line.split('当前所有可预约时间:')
                occur_time = lineprefix.split(',')[0].split(' ', 1)[-1]
                data[occur_time] = list(eval(times).keys())

        # 整合时间
        new_data = {}
        for occur_time, enable_times in data.items():
            new_occur_time = datetime.datetime.strptime(
                occur_time, '%Y-%m-%d %H:%M:%S').replace(second=0, microsecond=0)
            new_occur_time = new_occur_time - \
                relativedelta(minutes=new_occur_time.minute % 5)
            new_occur_time = new_occur_time.strftime('%Y%m%d%H%M%S')[:-2]
            new_data.setdefault(new_occur_time, set([])).update(set(enable_times))
        new_data = {str(key): list(value) for key, value in new_data.items()}

        # 时间排序
        last_data = {}
        for occur_time, enable_times in new_data.items():
            new_enable_times = []
            for enable_time in enable_times:
                enable_time_dt = datetime.datetime.strptime(enable_time, '%H:%M %A %B %d, %Y')
                new_enable_times.append(enable_time_dt.strftime('%Y%m%d%H%M%S')[:-2])
            last_data[occur_time] = sorted(new_enable_times)

        with open(new_filename, 'w') as fd:
            json.dump(last_data, fd, indent=2)

    available_files = glob.glob('*.txt')
    for available_file in available_files:
        new_json_file = available_file.rsplit('.')[0] + '.json'
        parse_and_save(available_file, new_json_file)


def generate_one_graph(title, image_file, data):
    """ 根据数据生成一张图标 """
    # X坐标(每一个监控时间点)
    columns = sorted(data.keys())
    y_offset = np.zeros(len(columns))
    # 构建二维表
    origin_data = {}
    max_length = 0  # Y轴最大高度
    for occur_time, avaliable_times in data.items():
        occur_index = columns.index(occur_time)

        if max_length < len(avaliable_times):
            max_length = len(avaliable_times)

        avaliable_time_map = {}
        for avaliable_time in avaliable_times:
            available_date = avaliable_time[:-2]
            avaliable_time_map[available_date] = avaliable_time_map.get(available_date, 0) + 1

        for available_date, num in avaliable_time_map.items():
            if available_date not in origin_data:
                origin_data[available_date] = [0 for _ in columns]
            origin_data[available_date][occur_index] = num
    values = np.arange(0, max_length, 5)
    value_increment = 1

    table_rows = []  # 表格各行名称
    rows = sorted(origin_data.keys())  # 表格中每一行
    for available_date in rows:
        table_rows.append(origin_data[available_date])
    # 设置每一行的颜色渐变
    c = np.linspace(0, 1, len(rows))
    plt.clf()
    colors = plt.cm.Dark2(c)
    colors = colors[::-1]
    # 设置
    n_rows = len(table_rows)
    index = np.arange(len(columns)) + 0.3
    bar_width = 0.4
    y_offset = np.zeros(len(columns))
    cell_text = []
    for row in range(n_rows):
        plt.bar(index, table_rows[row], bar_width, bottom=y_offset, color=colors[row])
        y_offset = y_offset + table_rows[row]
        cell_text.append(['%d' % x for x in y_offset])
    print('{} {} {}'.format(image_file, rows, columns))

    the_table = plt.table(cellText=cell_text,
                          rowLabels=rows,
                          rowColours=colors,
                          colLabels=columns,
                          loc='bottom')
    plt.rcParams.update({'figure.autolayout': True})
    plt.ylabel('可预约时间个数')
    plt.yticks(values * value_increment, ['%d' % val for val in values])
    plt.xticks([])
    plt.title(title)
    #  plt.show()
    plt.savefig('images/' + image_file, bbox_inches='tight')


def generate_graph():
    available_files = glob.glob('*.json')
    for available_file in available_files:
        #  if available_file not in ('上海-34490583.json', '广州-35980258.json', '上海-19815351.json'):
        #      continue
        avaliable_times = {}
        with open(available_file, 'r') as fd:
            avaliable_times = json.load(fd)

        title = available_file.rsplit('.', 1)[0]
        image_file = title + '.png'
        generate_one_graph(title, image_file, avaliable_times)


if __name__ == '__main__':
    parse()
    generate_graph()
