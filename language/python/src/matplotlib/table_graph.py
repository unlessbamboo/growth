#!/usr/bin/env python
# coding:utf8
import json
import numpy as np
import matplotlib.pyplot as plt


data = [
    [66386, 174296, 75131, 577908, 32015],  #
    [58230, 381139, 78045, 99308, 160454],
    [89135, 80552, 152558, 497981, 603535],
    [78415, 81858, 150656, 193263, 69638],
    [78415, 81858, 150656, 193263, 69638],
    [78415, 81858, 150656, 193263, 69638],
    [78415, 81858, 150656, 193263, 69638],
    [78415, 81858, 150656, 193263, 69638],
    [78415, 81858, 150656, 193263, 69638],
    [78415, 81858, 150656, 193263, 69638],
    [139361, 331509, 343164, 781380, 52269]
]

columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
rows = ['%d year' % x for x in range(0, len(data) * 5, 5)]

values = np.arange(0, 2500, 500)
value_increment = 1000

# Get some pastel shades for the colors
c = np.linspace(0, 1, len(rows))
colors = plt.cm.Dark2(c)
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.zeros(len(columns))

# Plot bars and create text labels for the table
cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
# Reverse colors and text labels to display the last value at the top.
colors = colors[::-1]

"""
[
    ['431.5', '1049.4', '799.6', '2149.8', '917.9'],
    ['292.2', '717.8', '456.4', '1368.5', '865.6'],
    ['213.8', '636.0', '305.7', '1175.2', '796.0'],
    ['124.6', '555.4', '153.2', '677.2', '192.5'],
    ['66.4', '174.3', '75.1', '577.9', '32.0']
]
"""
cell_text.reverse()

# Add a table at the bottom of the axes
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')
plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams.update({'figure.autolayout': True})

# Adjust layout to make room for the table:
#  plt.subplots_adjust(left=0.2, bottom=0.2)
#  plt.gcf().subplots_adjust(left=0.2, bottom=0.15)
#  plt.tight_layout()

plt.ylabel("Loss in ${0}'s".format(value_increment))
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Loss by Disaster')

#  plt.show()
plt.savefig('plot123_2.png', bbox_inches='tight')
