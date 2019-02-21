#!/bin/bash - 
#===============================================================================
#
#          FILE: ssr.sh
# 
#         USAGE: ./ssr.sh 
# 
#   DESCRIPTION:  监控shadowsocks-client, privoxy
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2019/01/15 15:25
#      REVISION:  --
#===============================================================================

PROJECT_PATH=$(dirname $(cd $(dirname "$0"); pwd))
RANDOM_NUM=0
SSL_CONFIGS=('ssl_usa.json' 'ssl_hk.json' 'ssl_app_server1.json' 'ssl_app_server2.json' 'ssl_app_server3.json')
SSL_CONFIGS_LENGTH=${#SSL_CONFIGS[@]}

existed_ssl=`ps -ef|grep sslocal|grep -v grep|grep python|grep monitor|grep config`
NEW_SERVER=${SSL_CONFIGS[0]}
for (( i=0 ;i <${SSL_CONFIGS_LENGTH}; i++ ));do
    if [[ ${existed_ssl} =~ ${SSL_CONFIGS[$i]} ]];then
        if [[ ${i} < $[${SSL_CONFIGS_LENGTH} - 1] ]];then
            NEW_SERVER=${SSL_CONFIGS[$[$i + 1]]}
        fi
    fi
done
echo "当前将要启动的代理服务器:" ${NEW_SERVER}


rand()
{
    min=0
    max=$(($1-${min}))
    num=$(date +%s)
    RANDOM_NUM=$((${num}%${max}+${min}))
}


start_sslocal()
{
    # sslocal_path=``whereis sslocal``
    sslocal_path='/home/myname/.local/bin/sslocal'

    ${sslocal_path} -c ${PROJECT_PATH}/config/${NEW_SERVER} >> /data/ssr/ss-local.log 2>&1 &
    if [[ $? != 0 ]];then
        echo "start sslocal:${ssl_config} failed!"
        exit -1
    fi
}


stop_sslocal()
{
    ps -ef|grep sslocal|grep -v grep|grep python|awk '{print $2}'|xargs kill -9 > /dev/null 2>&1
    if [[ $? != 0 ]];then
        echo "Stop sslocal failed"
        exit -1
    fi
}


check_sslocal()
{
    ps -ef|grep sslocal|grep -v grep|grep python
    if [[ $? == 0 ]];then
        echo "sslocal server aliving, needn't start"
        exit -1
    fi

    start_sslocal
    echo "Start sslocal successful"
}


check_privoxy()
{
    ps -ef|grep privoxy|grep -v grep|grep config
    if [[ $? == 0 ]];then
        echo "privoxy server aliving, needn't start"
        exit -1
    fi
    
    systemctl restart privoxy.service > /dev/null 2>&1
    if [[ $? != 0 ]];then
        echo "start privoxy failed!"
        exit -1
    fi

    systemctl -l status privoxy.service > /dev/null 2>&1
    if [[ $? != 0 ]];then
        echo "start privoxy failed!"
        exit -1
    fi
    echo "Start privoxy successful"
}



usage()
{
    echo "
        check           check sslocal and privoxy
        switch          auto switch sslocal
    "
}



# 自动切换代理
auto_switch()
{
    # 检查dst进程是否正在运行
    DST_LOG_FILE='/data/myname/dst/logs/dst_myname.log'

    succ=$false
    for i in `seq 1 600`;do
        last_modify_time=`stat -c %Y ${DST_LOG_FILE}`
        current_time=`date +%s`
        if [[ $[ ${current_time}-${last_modify_time} ] -lt 10 ]];then
            echo "dst正在运行中, 不能切换代理, 等待中..."
            sleep 2
        else
            succ=$true
            break
        fi
    done
    if [[ ${succ} ]];then
        echo "切换代理失败, 退出"
        sleep 1
    fi

    stop_sslocal
    start_sslocal
    echo "Auto switch sslocal success."
}


case ${1} in
    check)
        check_sslocal;
        check_privoxy;;
    switch)
        auto_switch;;
    *)
        usage;;
esac
