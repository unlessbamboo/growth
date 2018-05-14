---
title: 插件管理

time: 2017-05-12 07:53:50

tags: vim

---

# 1，GCC工作环境
## 1.1，Doxygen
### 1.1.1 Doxygen介绍
功能：对文件、类、函数、全局变量等进行简单说明，项目完成后，利用源代码以及其中的注释自动生成图文并茂的文档；
```
    相关工具：Rational SoDA，Doc++，Doxygen
    支持语言：C++、C、JAVA、python等
    搭配工具：graphviz，从而生成漂亮的类图
    PS：关于doxygen本身的配置不在这里描述，见以后的文章说明。
```

### 1.1.2 Doxygen配置
关于各个语言的Doxygen配置以后再了解，仅仅是用于文档的生成而已

### 1.1.3 DoxygenToolkit
适用语言：c/c++，对python不太合适

### 1.1.4 关联文档
见grocery-shop/../vim-doxygen.md文档的详细介绍


## 1.2，a.vim
### 1.2.1 功能
在.h/.cpp之间进行切换

### 1.2.2 命令
```vim
    "   a.vim模块：在.h/.cpp之间进行模块跳转
    "       A       在当前文件的.h/.cpp之间跳转
    "       AS      切割并打开.h文件
    "       AV      vertical切割
    "       AT      new tab and switch
    "       其他：  没用
    nmap <leader>as :A<cr> 
    nmap <leader>ass :AS<cr>
    nmap <leader>asv :AV<cr>
```


# 2，Shell工作环境
## 2.1，bashsupport
### 2.1.1 功能介绍
Write and run BASH-scripts using menus and hotkeys. Bash IDES
### 2.1.2 配置
见vimrc

## 2.2，shellcheck
### 2.2.1 功能介绍
A static analysis tool for shell scripts.
### 2.2.2 配置
需要和Syntastic配合使用


# 3，python环境
## 3.1，python-mode
目前已弃用。
一个vim中使用Python的综合解决方案（如果所有的语言都这样就Imaging）
Vim python-mode. PyLint, Rope, Pydoc, breakpoints from box.

## 3.2, rope
## 3.2.1 功能
代码重构和代码补全，其中代码补全功能和jedi会有冲突，需要注释前者
### 3.2.2 涉及库
```
    ropemode       帮助rope重构代码
    ropevim          使用rope库来进行代码重构和代码检查的插件
```

### 3.2.3 命令
```vim
    " turn off rope                    
    let g:pymode_rope=0
```

## 3.3，pylint
python代码的静态分析工具，功能远远大于flake8/pyflakes，但是出现好多警告，相比flake8，更加重。
### 3.3.1 检查项
    * 全局变量定义以及各式
    * 函数、方法、构造函数的参数数据
    * 字符串格式化信息
    * 不存在的类和属性
    * 不存在pydocstring

#### 3.3.2 配置
```vim
    " 关闭syntastic中对于py文件的检查
    let g:syntastic_ignore_files = ['\.py$']

    " disable python-mode's syntax checking
    let g:pymode_lint = 0
```

## 3.4，flake8
一个python模块，安装该模块会自动安装如下模块
    * pyflakes——静态检查python代码的逻辑错误
    * flake8——pep8风格的代码检查
    * pycodestyle——pep257以及其他py代码检查
    * mccabe——静态分析python代码的复杂度

## 3.5，jedi
python代码自动补全工具，快速高效的补全，用于Python-mode和YCM中
PS：对于不同的python版本，需要安装不同的jedi包

## 3.6，vim-pydocstring
Generate python docstring to your python scripts files.

## 3.7，整体方案
使用Syntastic+YCM替代python-mode，其中会涉及jedi/pylint/flake8；
pydocstring作为一个单独的插件进行文档的注释；


# 4，Html/CSS
## 4.1，emmet
老版本：Zen Coding
新版本：Emmet

## 4.2，emmet-vim
功能：在vim上使用emet；
中文文档：https://www.zfanw.com/blog/zencoding-vim-tutorial-chinese.html


# 5，markdown
## 5.1，markdown
```shell
    如果node没有安装，见插件管理-3中关于node的安装
    npm -g install instant-markdown-d
```

## 5.2，vim
### 5.2.1 插件
vim-instant-markdown
### 5.2.2 配置
```vim
    "zshrc的配置                                               
    set shell=bash\ -i                                         
    " 映射快捷键                                               
    let g:instant_markdown_autostart=0                         
    " 关闭自动开启浏览器的配置，使用命令:InstantMarkdownPreview                                                   
    let g:instant_markdown_slow=1                               
    map <silent> <leader>imp :InstantMarkdownPreview<cr> 
```


# 6，语法检查插件
##  6.1，synstatic
### 6.1.1 功能
* 用location list列出所有的错误
* 命令行窗口中显示当前的错误信息（相当于状态栏）
* 对于错误发生的行，会有错误标记信息，如警告、错误
* 状态栏会有标记信息
* 鼠标悬停在错误提示框中时，会出现错误提示框信息

### 6.1.2 原理
通过外部命令做语法检查，并把结果显示到vim中。
组成部分：
    * 语法检查插件. 配合外部命令完成特定文件特定命令的语法检查
    * 核心部分. 调度语法插件，并输出检查结果

### 6.1.3 命令和选项、checkers
见grocery-shop/knowledge/vim/syntastic.vimrc文件 
### 6.1.4 帮助文档命令
```vim
    " 文档
    help syntastic
    help syntastic-checkers
```

## 6.2，代码片段
### 6.2.1 ultisnips
在YCM中作为默认的competion interpreter.
### 6.2.2 vim-snippets
暂未了解，后期补全
### 6.2.3 vim-snipmate
以后了解


# 7，代码补全和跳转
## 7.1 ctags（标签）
### 7.1.1 功能介绍
功能：根据已经生成的标签文件，从而在vim中查看函数调用关系、类、结构、宏等各种定义，跳转于各个标签中
中文手册：http://easwy.com/blog/archives/exuberant-ctags-chinese-manual/

### 7.1.2 Tag文件格式
```shell
    ########################header################################
    tag文件的开头可以包含“!_TAGXXXX_”，用于加入额外的信息
    格式：!_TAG_FILE_SORTED<Tab>1<Tab>{anything}
        _TAG_FILE_SORTED表示tag文件是经过排序的（值为0——未经过排序，值为2——不分大小写排序，1——排序）
 
    ########################body################################
    格式：{tagname} {TAB} {tagfile} {TAB} {tagaddress} {term} {field} ..
            # field 可选字段，一般用于表示tagname的类型信息
            # tagfile 包含tagname的文件
            # tagaddress 可以定位到tagname光标位置的Ex命令，一般为行号或者搜索命令（哇，原来是这个原理）
            # term  设置为‘;’，用于兼容vi，使vi忽略后面的所有
            # tagname标识符名字，例如函数名、类名、结构名，但是不能包含制表符
```

### 7.1.3 命令
基本按键命令：
```vim
    " 查找某一个标签，如果找到会在quickfix（见下文）窗口中打开所有匹配的文件名
    tag <dststr>
    " 显示标签栈
    tags
    " 生成简单但是冗余的tags文件（宏，枚举变量，函数，类型定义，变量，类等）
    ctags -R *
    " 到定义处
    <c-]>
    " 返回前面的堆栈处
    <c-o>
    <c-T>
```

生成ctags的命令：
```vim
    " -c++kinds=+px       记录c++文件中的函数声明和各种外部和前向声明
    " –fields=+iaS        要求描述的信息
    " –extra=+q           强制要求ctags保证多个同名函数可以用不同路径区分
    " --exclude=@filename  忽略某些指定的文件以及目录

    " 指定当前目录下面的所有文件
    ctags -R –c++-kinds=+px –fields=+iaS –extra=+q .
    " 通过src.files文件列表指定，操作的源代码变为src.files源文件。
    ctags -R --c++-kinds=+px --fields=+iaS --extra=+q -L src.files
```

### 7.1.4 关于tags文件
考虑到开发过程中可能有多个项目（你自己的、公司的、python的、C的、C++的，也就我能这么奇葩，马蛋），所以
建议在每一个项目根目录下面放置XX.vim配置，进行个性化的导入（例如C则导入C库中的tags文件，python同理）

### 7.1.5 安装
#### 7.1.5.1 mac
```zshrc
    # 因为mac下的ctags不是exuberant ctags，所以要源码安装
    brew uninstall ctags
```

#### 7.1.5.2 源码
```shell
    # 下载 
    wget https://sourceforge.net/projects/ctags/files/ctags/# 安装
    tar -xvzf ctags-5.7.tar.gz 
    cd ctags-5.7/ 
    ./configure 
    make 
    sudo make install
    # 检查PATH路径
    # 请确保.vim/bundle/taglist都已经成功安装
```

## 7.2 cscope（查询）

## 7.3 YouCompleteMe(补全）
注意，其实该插件的跳转功能远远弱于ctags+cscope
### 7.3.1 文本自动补全
插件名称：acp, omnicppcomplete
原理：通过文本进行正则表达式的匹配（猜），再根据生成的tags来实现自动补全效果
### 7.3.2 基于语义补全：
插件名称：clang/llvm(apple)，YouCompleteMe
```shell
    代码层面原理：
        后端调用libclang从而获取AST以及其他语义分析库；    
        前端由C++开发以提高补全效率；
        外层使用python包装，提高一键化部署的能力；
    运行原理：
        CS模式
            C端：vim中开启的YCM是YCM中的一个很小的客户端，于具有大量逻辑和功能的server进行HTTP+JSON交互；
            S端：伴随开启和关闭vim而自动的启用
        python:
            对于python而言，需要在不同的开发环境下启用不同的jedi，使用https://github.com/vheon/JediHTTP.git来进行管理
```

## 7.4 tarbar
暂时未了解


# 8，版本控制
## 8.1 vim-gitgutter
git专用

## 8.2 signify
用于所有的版本控制，没有快捷键，仅仅记录版本修改信息

# 9 搜索
## 9.1 ag.vim
### 9.1.1 说明
shell终端命令：Ag(The Silver Searcher)
vim插件：ag.vim
功能：This plugin is front for Ag. Thisplugin will allow you run ag from vim, and shows the results in asplit window.
### 9.1.2 配置和命令
见vim_ag.md中的说明
### 9.1.3 安装
```zshrc
    # 安装automake
    brew install automake
    sudo aptitude install automake

    # 安装the_silver_searcher  
     brew install the_silver_searcher 
    sudo aptitude install silversearcher-ag
    # 安装ag.vim插件本身
    git submodule add https://github.com/rking/ag.vim bundle/ag.vim 
```


5，ctrlp

# 10 窗口
## 10.1 winmanager体系
后期删除，使用tarbar代替
### 10.1.1 netrw
说明：文件浏览插件，默认安装，vim7.0以前为exporer.vim插件，后来替换为netrw（FileExplorer）；
功能：使用vim尝试打开目录时，会自动调用netrw，获取目录下的文件列表，执行create/delete/update操作
### 10.1.2 bufexplorer
功能：Plugin for easilyexploring(资源管理器)vim：buffers
插件配置: BufExplorer介绍：快速浏览所有文件的buf插件，小型的文件缓存管理
```shell
     1）在光标指定到BufExplorer时（忽略）          
     2）命令模式下：                              
         bn       打开下一个buffer文件            
         bp       打开上一个buffer文件            
         b num    打开指定号码的文件              
         num1,num2bd 删除num1到num2之间的缓存      
     3）普通模式下：                              
         \bv      垂直打开一个窗口浏览所有的文件缓存
         \bs     水平打开（这是bufExplore的功能） 
     4) 关闭bufExplorer（前提是进入该窗口）：       
         d        删除单个缓冲文件                
         bd       删除所有缓冲文件                
         在会话保存中会用到（关闭所有动态窗口）     
```

### 10.1.3 winmanager
功能：集成管理Explorer、Bufexplorer、taglist插件，从而实现多窗口文件目录浏览操作
代码说明：
```shell
    plugin/winmanager.vim –winmanager插件
    plugin/winfileexplorer.vim  -改良的Explorer插件
    plugin/wintagexplorer.vim –winmanager提供的tag插件，用处不大
    doc/winmanager.txt – 帮助文件
    插件配置：具体配置与说明见vimrc
```

## 10.2 NERDTree古老的树体系
说明：显示当前目录以及子目录下的属性结构，用于浏览文件并打开指定的文件
配置：见vimrc
PS：用于寻找不知道文件具体名称的文件

## 10.3 lookupfile
后期使用ctrlp代替。
快速匹配查找并打开。
### 10.3.1 需求插件
ctags：在vim查看函数调用关系，类、结构、宏等的定义，可以在任意标签中跳转、返回，具体见后面章节
genutils：This script providesfunctions that are mostly userful to script developers.
同类插件：fuzzyfinder，lookupfile，ctrlp
### 10.3.2 安装
genutils和lookupfile，安装说明见《 vim-环境》说明，后面所有类似插件不再说明。
### 10.3.3 配置
```vim
    " <F5>开启窗口，输入bamboo.c +Enter，之后使用<C-N>,<C-P>选择   
    " 缓冲区浏览，在所有的缓冲区中寻找某个函数等，类似cscope
    LUBufs
    " 目录浏览
    LUWalk
    " 忽略大小写查找：\c或者\C                                    
    " PS:依赖genutils插件    
```
