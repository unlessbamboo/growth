#!/bin/bash - 

# 1. 检测
WAITING_SECOND=240
WAITING_INTERVAL=5
WAITING_NUM=`expr ${WAITING_SECOND}/${WAITING_INTERVAL}`
# cdbin在脚本中是否可执行? 如果cdbin目录找不到就直接写死
cdbin
if [[ $? != 0 ]];then
    # 本地测试请将目录更改为bin所在目录
    CDBIN_DIR=/home/upps/server/product/linux64/bin
    cd ${CDBIN_DIR}
else
    CDBIN_DIR=`pwd`
fi
echo $CDBIN_DIR

start_mgr_file='startMgr.sh'
if [[ ! -f ${CDBIN_DIR}/${start_mgr_file} ]];then
    echo "not found startMgr script:${CDBIN_DIR}/${start_mgr_file}"
    exit -1
fi
stop_mgr_file='stopMgr.sh'
if [[ ! -f ${CDBIN_DIR}/${stop_mgr_file} ]];then
    echo "not found stopMgr script:${CDBIN_DIR}/${stop_mgr_file}"
    exit -1
fi
list_mgr_file='listMgr.sh'
if [[ ! -f ${CDBIN_DIR}/${list_mgr_file} ]];then
    echo "not found listMgr script:${CDBIN_DIR}/${list_mgr_file}"
    exit -1
fi
# TOMCAT_DIR='/home/upps/tomcat/apache-tomcat-7.0.82/bin'
TOMCAT_DIR='/Users/bamboounuse/Public/meichuang/drcc-backend/bin'
if [[ ! -f ${TOMCAT_DIR}/start.sh ]];then
    echo "not found tomcat script:${TOMCAT_DIR}/start.sh"
    exit -1
fi


check_mgr() 
{
    # 怎么检测mgr是否启动成功? 根据脚本内容输出吗?
    ./${list_mgr_file}
    if [[ $? != 0 ]];then
        echo "mgr进程未启动"
        return -1
    fi
    echo "mgr进程已启动"
}


start_mgr()
{
    # a. 绝对路径方式
    # ${CDBIN_DIR}/${start_mgr_file}
    # b. 相对
    ./${start_mgr_file}
    if [[ $? != 0 ]];then
        echo "执行${start_mgr_file}脚本输出异常"
        return -1
    fi
}


stop_mgr()
{
    # a. 绝对路径方式
    # ${CDBIN_DIR}/${stop_mgr_file}
    # b. 相对
    ./${stop_mgr_file}
    if [[ $? != 0 ]];then
        echo "执行${stop_mgr_file}脚本输出异常"
        return -1
    fi
}


waiting_mgr_start()
{
    for ((i=1;i<${WAITING_NUM};i++));do
        check_mgr
        if [[ $? == 0 ]];then
            break
        fi
        echo "----------"
        sleep ${WAITING_INTERVAL}
    done
    check_mgr
    if [[ $? != 0 ]];then
        return -1
    fi
}


waiting_mgr_stop()
{
    for ((i=1;i<${WAITING_NUM};i++));do
        check_mgr
        if [[ $? != 0 ]];then
            break
        fi
        sleep ${WAITING_INTERVAL}
    done
    check_mgr
    if [[ $? == 0 ]];then
        return -1
    fi
}


start_tomcat()
{
    ${TOMCAT_DIR}/start.sh
    if [[ $? != 0 ]];then
        echo "执行脚本${TOMCAT_DIR}/start.sh异常"
        return -1
    fi
    echo "等待tomcat启动..."
}


stop_tomcat()
{
    # 匹配tomat进程并杀死, 这个用户提供下, 例如: ps -ef|grep tomcat|grep -v grep|awk '{print $2}'|xargs kill -9
    echo "stop tomcat"
}


# 2. 判断mgr是否已经启动
check_mgr
if [[ $? != 0 ]];then
    # 启动startMgr
    start_mgr
    if [[ $? != 0 ]];then
        exit -1
    fi
    # 检测mgr是否启动成功
    waiting_mgr_start
    if [[ $? != 0 ]];then
        exit -1
    fi
fi
# 3. 启动tomcat 
start_tomcat
