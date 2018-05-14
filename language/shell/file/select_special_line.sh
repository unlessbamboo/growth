#!/bin/bash - 
#===============================================================================
#
#          FILE: select_special_line.sh
# 
#         USAGE: ./select_special_line.sh 
# 
#   DESCRIPTION: 获取文件中的指定行并打印
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2018/05/11 23:00
#      REVISION:  ---
#===============================================================================


filename='file.txt'

# 获取文件中的指定行
sed -n 10p ${filename}
