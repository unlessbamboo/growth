#!/bin/bash - 
#===============================================================================
#
#          FILE: tmux.sh
# 
#         USAGE: ./tmux.sh
# 
#   DESCRIPTION: 
#           tmux 配置
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: The current file is dependent upon update_local
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2017-05-21 00:02:00
#      REVISION:  ---
#===============================================================================

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  err
#   DESCRIPTION:  display err msg
#    PARAMETERS:  
#       RETURNS:  
#-------------------------------------------------------------------------------
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


#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  _update_local
#   DESCRIPTION:  
#           拷贝当前子目录到$HOME/.local目录下
#    PARAMETERS:  
#       RETURNS:  
#-------------------------------------------------------------------------------

_update_tmux()
{
    tmux_dir=$(pwd)/"tmux"
    dst_dir="$HOME/.local/tmux"

    if [[ -d ${dst_dir} ]];then
        rm ${dst_dir}
    fi

    if [[ -d ${tmux_dir} ]];then
        ln -sf ${tmux_dir} $HOME/.local/
        if [[ $? != 0 ]];then
            err "Copy ${tmux_bin} to ~/.local/ failed."
        fi
    fi
}


_update_tmuxinator()
{
    tmuxinator_dir="tmuxinator"
    dst_dir=$HOME/.${tmuxinator_dir}
    if [[ -d ${dst_dir} ]];then
        mv ${dst_dir} /tmp/
    fi

    if [[ -d ${tmuxinator_dir} ]];then
        ln -sf $(pwd)/${tmuxinator_dir} ${dst_dir}
        if [[ $? != 0 ]];then
            err "Copy ${tmuxinator_dir} to ~/ failed."
        fi
    fi
}


_update_tmux
_update_tmuxinator
