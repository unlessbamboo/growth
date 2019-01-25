#!/usr/bin/env python
# coding:utf8
import numpy as np
import matplotlib.pyplot as plt


N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups, X轴个数
# the width of the bars: can also be len(x) sequence, 每一个柱状图的宽度
width = 0.35

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width, bottom=menMeans, yerr=womenStd)
p3 = plt.bar(ind, menMeans, width, yerr=menStd)
p4 = plt.bar(ind, womenMeans, width, bottom=menMeans, yerr=womenStd)
p5 = plt.bar(ind, menMeans, width, yerr=menStd)
p6 = plt.bar(ind, womenMeans, width, bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0]),
           ('Men', 'Women', '3', '4', '5'))

plt.show()
