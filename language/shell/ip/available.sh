#!/bin/bash - 
#===============================================================================
#
#          FILE: available.sh
# 
#         USAGE: ./available.sh 
# 
#   DESCRIPTION: 
#           查询当前网段内所有在线的 IP, 利用ping即可达到效果
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2017/11/01 21:18
#      REVISION:  ---
#===============================================================================

for ip in 192.168.31.{1..255};
do
    # echo "----- ${ip}"
    sleep 0.2
    (
        ping $ip -c2 &> /dev/null
        if [ $? -eq 0 ];
        then
            echo "$ip 在线"
        fi
    )&
done

wait
