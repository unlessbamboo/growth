#!/bin/bash - 
#===============================================================================
#
#          FILE: listMgr.sh
# 
#         USAGE: ./listMgr.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2022/06/14 22:07
#      REVISION:  ---
#===============================================================================


ps -ef|grep redis|grep -v grep
