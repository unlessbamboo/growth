#!/bin/bash - 
#===============================================================================
#
#          FILE: webserver.sh
# 
#         USAGE: ./webserver.sh 
# 
#   DESCRIPTION: 初始化Docker环境
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: ---
#      REVISION:  ---
#===============================================================================


centos_docker_start()
{
    centos_version=$1
    if [[ $centos_version == 7 ]];then
        sudo systemctl enable docker
        sudo systemctl start docker
    else
        sudo service docker start
    fi

    # 添加docker用户
    sudo groupadd docker
    sudo usermod -aG docker $USER
}


centos() 
{
    # 卸载旧版本
    sudo yum remove docker \
        docker-client \
        docker-client-latest \
        docker-common \
        docker-latest \
        docker-latest-logrotate \
        docker-logrotate \
        docker-selinux \
        docker-engine-selinux \
        docker-engine
    if [[ $? != 0 ]];then
        echo "卸载docker环境失败"
        exit -1
    fi
    # 安装docker
    # curl -fsSL get.docker.com -o get-docker.sh
    # sudo sh get-docker.sh --mirror Aliyun

    # 安装依赖包
    sudo yum install -y yum-utils \
       device-mapper-persistent-data \
       lvm2
    # 添加源
    sudo yum-config-manager \
        --add-repo \
        https://mirrors.ustc.edu.cn/docker-ce/linux/centos/docker-ce.repo
    sudo yum-config-manager --enable docker-ce-edge
    # 更新yum缓存
    sudo yum makecache -y fast
    if [[ $? != 0 ]];then
        echo "更新yum软件源失败"
        exit -1
    fi
    # 安装
    sudo yum install -y docker-ce

    # 启动docker
    centos_version=`rpm -qa \*-release | grep -Ei "oracle|redhat|centos" | cut -d"-" -f3`
    centos_docker_start $centos_version

    # 测试是否安装成功
    docker run hello-world
    if [[ $? != 0 ]];then
        echo "docker测试失败, 请重新安装"
        exit -1
    fi

    echo "安装docker环境成功"
}


ubuntu_docker_start()
{
    ubuntu_version=$1
    # 启动
    if [[ $ubuntu_version == "16" ]];then
        sudo systemctl enable docker
        sudo systemctl start docker
    else
        sudo service docker start
    fi
    
    # 添加docker用户
    sudo groupadd docker
    sudo usermod -aG docker $USER

}


ubuntu()
{
    # 卸载旧包
    sudo apt-get remove -y docker \
        docker-engine \
        docker.io
    ubuntu_version = `lsb_release -r -s | cut -d"." -f1`
    # 对于14.04, 安装可选内核模块
    if [[ $ubuntu_version == "14" ]];then
        sudo apt-get install \
            linux-image-extra-$(uname -r) \
            linux-image-extra-virtual
        if [[ $? != 0 ]];then
            echo "在ubuntu14.04上安装内核模块失败"
            exit -1
        fi
    fi
    # 安装证书
    sudo apt-get install -y \
        apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common
    if [[ $? != 0 ]];then
        echo "安装CA证书失败"
        exit -1
    fi
    # 添加源
    curl -fsSL https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository \
        "deb [arch=amd64] https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
    # 安装
    sudo apt-get install -y docker-ce

    # 启动
    ubuntu_docker_start $ubuntu_version

    # 测试
    docker run hello-world
    if [[ $? != 0 ]];then
        echo "docker测试失败, 请重新安装"
        exit -1
    fi
    echo "安装docker环境成功"
}


# 开发或者测试环境, 使用官方脚本自动化安装
dev()
{
    curl -fsSL get.docker.com -o get-docker.sh
    sudo sh get-docker.sh --mirror Aliyun
    if [[ $? != 0 ]];then
        echo "Docker安装失败"
        exit -1
    fi
    # 启动和添加docker用户参考ubuntu/centos
    if [[ $1 == "ubuntu" ]];then
        # 启动
        ubuntu_version = `lsb_release -r -s | cut -d"." -f1`
        ubuntu_docker_start $ubuntu_version
    else
        centos_version=`rpm -qa \*-release | grep -Ei "oracle|redhat|centos" | cut -d"-" -f3`
        centos_docker_start $centos_version
    fi
}


usage()
{
    echo "
        centos          Install docker on centos.
        ubuntu          Install docker on ubuntu.
        dev             Install docker develop environment.
    "
}


case "$1" in
    centos):
        centos;;
    ubuntu):
        ubuntu;;
    dev):
        dev $2;;
    *):
        usage;;
esac
