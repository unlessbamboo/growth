#!/bin/bash - 
#===============================================================================
#
#          FILE: parse.sh
# 
#         USAGE: ./parse.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2022/03/17 11:38
#      REVISION:  ---
#===============================================================================

declare -A CONFIG_VALUES

CONFIG_FILE=./.env_file
CONFIG_VALUES=()

# 读取配置并复制给CONFIG_VALUES variables
function read_config() {
    while read LINE;do
        AIM=${LINE%=*}
        if [ -z ${AIM} ];then
            continue
        fi

        CONFIG_VALUES["${AIM}"]=`echo ${LINE#*=}`
    done
}
