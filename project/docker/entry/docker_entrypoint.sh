#!/bin/bash - 
#===============================================================================
#
#          FILE: docker-entrypoint.sh
# 
#         USAGE: ./docker-entrypoint.sh 
# 
#   DESCRIPTION: 基于传递过来的命令行参数, 进行不同的打印服务
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2018/04/25 15:23
#      REVISION:  ---
#===============================================================================


if [[ $1 == "echo" ]];then
    echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    echo "I am superman!"
    echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
elif [[ $1 == "show" ]];then
    ls -la
    ls -l /
else
    echo "Why? What? Shit!"
fi
