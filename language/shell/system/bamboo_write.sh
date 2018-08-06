#!/bin/bash - 
#===============================================================================
#
#          FILE: bamboo.sh
# 
#         USAGE: ./bamboo.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2018/07/19 15:45
#      REVISION:  ---
#===============================================================================

start()
{
    /usr/bin/python $HOME/Growth/language/shell/system/bamboo_write.py > /dev/null 2>&1 &
}


stop()
{
    ps -ef|grep bamboo|grep -v grep|grep -v vim|awk '{print $2}'|xargs kill -9 > /dev/null 2>&1
}


restart()
{
    stop
    start
}


case ${1} in
    start)
        start;;
    stop)
        stop;;
    restart)
        restart;;
    *)
        stop;;
esac


