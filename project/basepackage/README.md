---
title: "基础包模块"

description: "该项目为毕业初期一个基础模块的打包记录"

---


### 1 说明
功能：提供基础包模块

说明： 包中所有文件都是已经经过setuptools处理后的文件，安装即可

安装：

```sh
# 1）系统默认的python环境
python setup.py install
    
# 2）指定新的python路径
export PYTHONPATH=$PYTHONPATH:prefixDir
python setup.py install --prefix=prefixDir

# 例如安装到test1目录
export PYTHONPATH=~/test1/lib/python2.6/:$PYTHONPATH
python setup.py install --prefix=~/test1/
```

使用： 安装成功后，即可正常使用该模块，具体见测试代码

配置：

```txt
    basepackage模块存在一些配置，安装后，会存在以下目录：
        配置文件目录 ：/data/logs/job/
    该目录以及子文件位置不能发生更改，不过你可以更改配置中的Key-value值
    来自定义的设置数据目录、日志目录。
```

### 2 ChangeLog
#### 2.1 V1.0
初版, 很多年前的代码, 都忘了.

#### 2.2 V2.0
python: Python3.6
代码: 部门代码格式变动, 其他功能基本保持不变, 此次改动主要是为了整理下setup打包的流程
