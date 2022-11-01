
#!/bin/bash
# File Name: iconv.sh
# Author: wanggy
# site: www.jb51.net
#
show_file()
{
    for file in `ls $1`
    do
        if [ -d $1"/"$file ];then
            #目录递归调用show_file函数
            show_file $1"/"$file
        else
            #文件
            echo $1"/"$file
            file_type=`file $1"/"$file`
            type=`echo $file_type |grep UTF-8`
            if [ -z "$type" ];then
                echo "为空非utf-8编码，转换"
                iconv -f GB2312 -t utf8 $1"/"$file -o $1"/"$file
            else
                echo "utf8编码不用转换"
            fi
        fi
    done
}
path=/Users/bamboounuse/Public/css/html/html
show_file $path

