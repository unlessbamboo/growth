#!/bin/bash - 
#===============================================================================
#
#          FILE: check_system.sh
# 
#         USAGE: ./check_system.sh 
# 
#   DESCRIPTION: 检查系统类型
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2018/07/06 15:32
#      REVISION:  ---
#===============================================================================



#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  isroot
#   DESCRIPTION:  判断路径, 以及检查是否为root用户
#    PARAMETERS:  
#       RETURNS:  
#-------------------------------------------------------------------------------
isroot()
{
    PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
    export PATH

    #Check Root
    [ $(id -u) != "0" ] && { echo "${CFAILURE}Error: You must be root to run this script${CEND}"; exit 1; }
}


OS=""
OS_VERSION=0
#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  system_version
#   DESCRIPTION:  获取当前运行系统以及版本信息
#    PARAMETERS:  
#       RETURNS:  
#-------------------------------------------------------------------------------
system_version()
{
    #Check OS
    if [ -n "$(grep 'Aliyun Linux release' /etc/issue 2>/dev/null)" -o -e /etc/redhat-release ]; then
        OS=CentOS
        [ -n "$(grep ' 7\.' /etc/redhat-release)" ] && CentOS_RHEL_version=7
        [ -n "$(grep ' 6\.' /etc/redhat-release)" -o -n "$(grep 'Aliyun Linux release6 15' /etc/issue)" ] && CentOS_RHEL_version=6
        [ -n "$(grep ' 5\.' /etc/redhat-release)" -o -n "$(grep 'Aliyun Linux release5' /etc/issue)" ] && CentOS_RHEL_version=5
    elif [ -n "$(grep 'Amazon Linux AMI release' /etc/issue 2>/dev/null)" -o -e /etc/system-release ]; then
        OS=CentOS
        OS_VERSION=6
    elif [ -n "$(grep bian /etc/issue 2>/dev/null)" -o "$(lsb_release -is 2>/dev/null)" == 'Debian' ]; then
        OS=Debian
        [ ! -e "$(which lsb_release)" ] && { apt-get -y update; apt-get -y install lsb-release; clear; }
        OS_VERSION=$(lsb_release -sr | awk -F. '{print $1}')
    elif [ -n "$(grep Deepin /etc/issue 2>/dev/null)" -o "$(lsb_release -is 2>/dev/null)" == 'Deepin' ]; then
        OS=Debian
        [ ! -e "$(which lsb_release)" ] && { apt-get -y update; apt-get -y install lsb-release; clear; }
        OS_VERSION=$(lsb_release -sr | awk -F. '{print $1}')
    elif [ -n "$(grep Ubuntu /etc/issue 2>/dev/null)" -o "$(lsb_release -is 2>/dev/null)" == 'Ubuntu' -o -n "$(grep 'Linux Mint' /etc/issue 2>/dev/null)" ]; then
        OS=Ubuntu
        [ ! -e "$(which lsb_release)" ] && { apt-get -y update; apt-get -y install lsb-release; clear; }
        OS_VERSION=$(lsb_release -sr | awk -F. '{print $1}')
        [ -n "$(grep 'Linux Mint 18' /etc/issue)" ] && OS_VERSION=16
    elif [ "$(uname 2>/dev/null)" = "Darwin" ];then
        OS=MacOS
        OS_VERSION=$(uname -a|awk '{print $3}')
    else
        echo "${CFAILURE}Does not support this OS, Please contact the author! ${CEND}"
        # 删除自身应用进程
        kill -9 $$
    fi
}



PHYSICAL_CPU=0
PHYSICAL_CORE_CPU=0
THREAD=0
#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  cpuinfo
#   DESCRIPTION:  获取当前物理CPU个数, 每一个CPU上的核数, 逻辑CPU个数, 注意超线程技术仅仅适用于Linux
#    PARAMETERS:  
#       RETURNS:  
#-------------------------------------------------------------------------------
cpuinfo()
{
    if [[ ${OS} == 'MacOS' ]];then
        PHYSICAL_CPU=$(sysctl hw.physicalcpu|awk '{print $2}')
        PHYSICAL_CORE_CPU=$(sysctl hw.logicalcpu|awk '{print $2}')
        THREAD=$(sysctl hw.logicalcpu|awk '{print $2}')
    else
        PHYSICAL_CPU=$(grep 'physical id' /proc/cpuinfo | sort -u)
        PHYSICAL_CORE_CPU=$[$(grep 'core id' /proc/cpuinfo | sort -u | wc -l) * ${PHYSICAL_CPU}]
        THREAD=$(grep 'processor' /proc/cpuinfo | sort -u | wc -l)
    fi
}



# 定义终端颜色
red='\033[0;31m'
green='\033[0;32m'
yellow='\033[0;33m'
plain='\033[0m'

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  show
#   DESCRIPTION:  显示各个变量值
#    PARAMETERS:  
#       RETURNS:  
#-------------------------------------------------------------------------------
show()
{
    echo "系统信息: ${OS}"
    echo "系统版本: ${OS_VERSION}"

    echo "物理CPU个数: ${PHYSICAL_CPU}"
    echo "逻辑CPU个数: ${THREAD}"
}


main()
{
    clear
    echo '-------------------------------'
    echo 'Func: 获取系统信息'
    echo 'Author: unlessbamboo@gmail.com'
    echo '-------------------------------'
    echo ""

    # 是否为root
    isroot
    # 获取系统版本
    system_version
    # CPU信息
    cpuinfo
    show
}
main
