#!/bin/bash - 
#===============================================================================
#
#          FILE: tools.sh
# 
#         USAGE: ./tools.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2017/08/26 20:03
#      REVISION:  ---
#===============================================================================

err()                                                                           
{
    local   stdfile="/data/log/bamboo-install.log"
    if [[ ! -f "${stdfile}" ]];then
        touch "${stdfile}"
    fi
    echo "+++++++[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $@"
    echo "+++++++[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $@" >>"${stdfile}"
    exit 1
}


relink_tool()
{
    local subArr=("crontab")
    for dir in "${subArr[@]}";do
        cd ${dir}
        ln -sf $(pwd)/* $HOME/.local/bin/
        if [[ $? != 0 ]];then
            err "Copy ${dir} to ~/.local/ failed."
        fi
        cd -
    done
}


relink_tool
