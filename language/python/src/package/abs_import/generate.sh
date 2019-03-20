#!/bin/bash - 

pyinstaller --clean --noconfirm --windowed --onefile pkg.spec
if [[ $? != 0 ]];then
    echo "打包失败"
    exit -1
fi
