#!/bin/bash - 
#===============================================================================
#
#          FILE: scope_test.sh
# 
#         USAGE: ./scope_test.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2021/12/19 15:38
#      REVISION:  ---
#===============================================================================


name="global"


function fun1() {
    echo ${name}
}


function fun2() {
    local name="func2"
    fun1
}


fun1
echo "xxxxxxxxxxxxxxx"
fun2
