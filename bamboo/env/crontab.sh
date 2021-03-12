#!/bin/bash - 
#===============================================================================
#
#          FILE: crontab.sh
# 
#         USAGE: ./crontab.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2021/03/12 14:11
#      REVISION:  ---
#===============================================================================


# 1. 更新homebrew
ibrew_echo=`which ibrew`
abrew_echo=`which abrew`
brew_echo=`which brew`
if [[ ! $ibrew_echo =~ "not found" ]];then
    ${ibrew_echo} update
elif [[ ! $abrew_echo =~ "not found" ]];then
    abrew update
elif [[ ! $brew_echo =~ "not found" ]];then
    brew update
fi

