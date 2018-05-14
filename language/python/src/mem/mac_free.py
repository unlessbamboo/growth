# coding:utf8
'''
Created on Jun 1, 2014

@author: jay
'''

import subprocess
import re

# Get process info
ps = subprocess.Popen(['ps', '-caxm', '-orss,comm'],
                      stdout=subprocess.PIPE).communicate()[0]
vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0]

# Iterate processes
processLines = ps.split('\n')
sep = re.compile(r'[\s]+')
rssTotal = 0  # kB
for row in range(1, len(processLines)):
    rowText = processLines[row].strip()
    rowElements = sep.split(rowText)
    try:
        rss = float(rowElements[0]) * 1024
    except Exception:
        rss = 0  # ignore...
    rssTotal += rss

# Process vm_stat
vmLines = vm.split('\n')
sep = re.compile(r':[\s]+')
vmStats = {}
for row in range(1, len(vmLines) - 2):
    rowText = vmLines[row].strip()
    rowElements = sep.split(rowText)
    vmStats[(rowElements[0])] = int(rowElements[1].strip('.')) * 4096

print '系统核心使用, 永远不会删除, Wired Memory:\t\t%d MB' % (
    vmStats["Pages wired down"] / 1024 / 1024)
print '正在被使用的内存, Active Memory:\t\t%d MB' % (
    vmStats["Pages active"] / 1024 / 1024)
print '被分配但未使用内存, Inactive Memory:\t%d MB' % (
    vmStats["Pages inactive"] / 1024 / 1024)
print '可分配内存, Free Memory:\t\t%d MB' % (vmStats["Pages free"] / 1024 / 1024)
print 'Real Mem Total (ps):\t%.3f MB' % (rssTotal / 1024 / 1024)
