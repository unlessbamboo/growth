#!/bin/bash - 
#===============================================================================
#
#          FILE: execute_after_sleep.sh
# 
#         USAGE: ./execute_after_sleep.sh 
# 
#   DESCRIPTION: 简单的定时执行
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2018/06/01 16:01
#      REVISION:  ---
#===============================================================================


MAX_NUM=1000

for i in $(seq 1 ${MAX_NUM});do
    echo "----------${i}-----------"
    curl -vX POST -H @/data/data/save_status.head --data @/data/data/save_status.json http://127.0.0.1:5000/api/v2/save/status
    echo "----------end-----------"
    echo
    echo
    sleep 5
done
