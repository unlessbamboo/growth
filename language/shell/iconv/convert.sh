#!/bin/bash - 
#===============================================================================
#
#          FILE: convert.sh
# 
#         USAGE: ./convert.sh 
# 
#   DESCRIPTION: 
#       参考https://github.com/alkimake/batch-encoding-convert/blob/master/linux/convert.sh
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2022/03/31 22:35
#      REVISION:  ---
#===============================================================================

# converts xml and java files
DIR=$1
OLD_ENCODE="GB2312"

for i in $(find $DIR -name '*.xml' -or -name '*.java'); do
 iconv -f "${OLD_ENCODE}" -t "UTF8" $i -o $i;
done

