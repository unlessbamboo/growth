#!/bin/bash - 
#===============================================================================
#
#          FILE: backup_log.sh
# 
#         USAGE: ./backup_log.sh 
# 
#   DESCRIPTION: 备份日志, 在确保服务正常运行的前提下, 直接备份日志, 并清空原日志文件
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2018/06/11 10:08
#      REVISION:  ---
#===============================================================================

BAMBOO_DIR='/data/visa'
BACKUP='backup'
SCHEDULE_BAMBOO_DIR="${BAMBOO_DIR}/schedule_visa/logs"


backup_logs()
{
    origin_log=$1
    backup_dir=$2
    backup_log="${backup_dir}/`basename ${origin_log}`.`date +%F`"

    if [[ -f ${backup_log} ]];then
        echo "已经存在备份文件:${backup_log}, 避免日志数据丢失, 直接退出日志备份"
        return -1
    fi

    mv ${origin_log} ${backup_log} && echo "">${origin_log}
    if [[ $? != 0 ]];then
        echo "备份日志文件失败."
        return -1
    fi
}


schedule()
{
    backup_dir=${SCHEDULE_BAMBOO_DIR}/${BACKUP} 
    if [[ ! -d ${backup_dir} ]];then
        mkdir -p ${backup_dir}
    fi

    # scrapy
    for bamboo in `ls ${SCHEDULE_bamboo_DIR}/bamboo_schedule_* 2>/dev/null`;do
        backup_logs ${scrapy} ${backup_dir}
    done

    # info
    info_log=${SCHEDULE_BAMBOO_DIR}/schedule_visa.log
    if [[ -f ${info_log} ]];then
        backup_logs ${info_log} ${backup_dir}
    fi
    # debug
    info_log=${SCHEDULE_BAMBOO_DIR}/schedule_visa_debug.log
    if [[ -f ${info_log} ]];then
        backup_logs ${info_log} ${backup_dir}
    fi
}


main()
{
    schedule
}
main
