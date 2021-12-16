#!/bin/bash - 
#===============================================================================
#
#          FILE: a.sh
# 
#         USAGE: ./a.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2021/12/15 22:52
#      REVISION:  ---
#===============================================================================

# 转换编码方法
function transferFile ()
{
    
  for file in `ls $1`
  do
    if [ -d $1"/"$file ]
    then
      transferFile $1"/"$file
    else
      fileName=`echo $1"/"$file`
      fileType=${fileName##*.}
      originType="GB2312"
      newType="UTF-8"
      # 将文件夹内的html和htm文件从GB2312转为UTF-8
      echo $fileName
      iconv -f $originType -t $newType $fileName -o $fileName > /dev/null 2>&1
      # if [[ $fileType = "html" || $fileType = "htm" ]]
      # then
      #   echo $fileName
      #   iconv -f $originType -t $newType $fileName -o $fileName > /dev/null 2>&1
      # fi
    fi
  done
}

# 需要转码的文件夹
folder="src"
transferFile $folder

