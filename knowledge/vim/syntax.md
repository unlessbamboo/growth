---
title: 基本语法和基本插件

date: 2017-05-02 08:00:30 

tags: vim

filename: vim/syntax.md

---

> 所有ex-[command]，实际命令为ex命令(:[command])


## 1 系统与安装
### 1.1 参考
```txt
    tags：  
        http://easwy.com/blog/archives/advanced-vim-skills-catalog/
    syntastic：
        http://note.hackrole.com/drafts/vim_config_syntastic.html
        https://github.com/scrooloose/syntastic
```

### 1.2 unix
```bash
    # ubuntu
    sudo aptitude update
    sudo aptitude install vim

    # mac
    export PATH=/usr/local/bin:$PATH
    brew update
    brew install vim && brew install macvim
    brew linkapps macvim

    # 查看是否支持系统剪贴板（不要在tmux-0窗口打开）
    vim --version | grep clipboard
```

### 1.3 windows
```txt
    # 文件夹
    vimfiles：初次安装结束后会有很多空文件夹，建议删除，一边后面安装插件时更加一目了然
    _vimrc：类似于Linux上的.vimrc文件
    PS：如果vim按照在系统盘中，注意更改整个vim文件夹的属性，不然_vimrc无法正常的更改

    # 启动
    gvim

```

## 2 文件自动检测
检测欲编辑的文件类型，通过文件名或者文本中特定的字符来判定。
### 2.1 filetype
```vim
    " 设置
    filetype plugin indent on

    " 查看当前filetype配置，在《命令行》模式下
    filetype
```

### 2.2 命令说明
```vim
    " 开启文件检测
    filetype on

    " 允许特定的文件类型插入插件
    " 过程：在runtimepath中搜索指定类型的所有插件（python/c etc），然后执行
    filetype plugin on

    " 相应的插件不会自动载入，如果你关闭特定文件类型检测
    filetype plugin off
    
    " runtimepath的路径在UNIX中为：
    " $HOME/.vim、$vim/vimfiles、$vimRUNTIME

    " 为特定的文件类型载入《缩进文件》
    " 过程：载入runtimepath中的$vimRUNTIME/indent.vim脚本来完成
    filetype indent on
```

### 2.3 应用实例：
```vim
    " 通过lookupfile.vim插件来自动的关闭缓冲区, 新建runtimepath/ftplugin目录，
    " 新建lookupfile.vim
    " close lookupfile window by two <Esc
    nnoremap <buffer <Esc<Esc <C-Wq
    inoremap <buffer <Esc<Esc <Esc<C-Wq
```

## 3 autocmd
详细说明见:help autocmd<br/>
在文件读写、缓冲区或者窗口进出，vim退出时刻，指定自动执行的命令。<br/>
autocmd——自动命令，当某些事件发生时（文件读入/改变缓冲区,etc），自动执行。
### 3.1 命令格式
#### 3.1.1 添加自动命令
```txt
    au[tocmd] [group] {events} {pat} [nested]  {command}
        group               可选项，管理和调用命令
        events              触发事件列表，用逗号隔开
        pat                 文件命令，通常伴随通配符，目标文件类型
        nested              允许自动命令的嵌套使用
        command             欲被执行的命令

    执行流程：
        将{command}加到vim在匹配{pat}模式的文件执行{evernt}事件时“自动执行”的那个命令列表中。
    
    事件：
        各种具体的操作触发事项见<http://vimcdoc.sourceforge.net/doc/autocmd.html>说明

    匹配模式：
        类似shell的模糊匹配
            如果模式中没有'/'，仅仅匹配文件名的尾部，不包括目录路径
            如果模式中有'/'，匹配完整路径

    缓冲区：
        <buffer>                    当前缓冲区
        <buffer=99>                 缓冲区号 99
        <buffer=abuf>               在自动命令中生效

    调试：
        测试自动命令的时候，set verbose=9，可以回显自动命令，非常有用
```

**例子**：
```vim
    " Open a new file with: edit foo and close it right way with :quit. Look on your hard drive and you'll
    " notice that the file is not there. Let's change it
    " BufNewFile ----- the 'event' to watch for.
    " * ----- a 'pattern' to filter the event
    " :write ----- the command to run
    autocmd BufNewFile * ex-command

    " Handle txt suffix file
    autocdmd BufNewFile *.txt ex-write

    " 使用normal命令（一般在vim script使用，执行normal命令）
    " 类似：光标调到末尾
    normal G
    " 在文件保存的时候，自动执行“=”命令
    autocmd BufWritePre *.html ex-normal gg=G


    " Multiple events by separating the events with a comma
    autocmd BufWritePre,BufRead *.html ex-normal gg=G


    " FileType events --- Fired whenever vim sets a buffer's filetype
    " Most useful events
    " 打开.js文件，按,c会注释当前行
    autocmd FileType javascript nnoremap <buffer> <localleader>c I//<esc>
    " 打开.py文件，注释某一行
    autocmd FileType python     nnoremap <buffer> <localleader>c I#<esc>


    " 删除当前缓冲区的局部于缓冲区的自动命令
    au! * <buffer>
    " 列出当前缓冲区的局部于缓冲区的自动命令
    au * <buffer>
    " 测试局部于缓冲区的自动命令是否存在
    if exists("#GroupName#<buffer=12>") | ... | endif
```

#### 3.1.2 删除自动命令
**格式**:
```txt
    au[tocmd]! [group] {event} {pat} {nested} {cmd}
                删除所有和{event}，{pat}关联的自动命令，之后加入新的{cmd}到{group}中

    au[tocmd]! [group] {event} {pat}
                删除所有关联的自动命令

    au[tocmd]! [group] * {pat}
    au[tocmd]! [group] {event}
    au[tocmd]! [group]
```

#### 3.1.3 列出自动命令
```txt
    au[tocmd] [group] {event} {pat}
                列出关联的命令，不添加命令
    
    au[tocmd] [group] * {pat}
    au[tocmd] [group] {event}
```

### 3.2 组
定义分组之后，所有的自动命令都会自动在内存中被重新分组，从而高效的
对某一个分组进行操作（删除等）。
```vim
    " 命令
    augroup cprograms
        autocmd BufReadPost *.c,*.h set sw=4 sts=4
        autocmd BufReadPost *.cpp   set sw=3 sts=3
    augroup END
    " 等价于
    autocmd cprograms BufReadPost *.c,*.h set sw=4 sts=4
    autocmd cprograms BufReadPost *.cpp   set sw=3 sts=3
```

### 3.4 嵌套
一般而言，一个事件触发的自动命令执行之后，便不会再次触发其他事件，
这是不利的，所以产生nested
``` vim
    autocmd FileChangedShell * nested edit 
```

### 3.5 忽略事件
忽略事件列表中所有事件的触发
``` vim
    " 事件列表
    set eventignore=WinEnter,WinLeave
    " 所有事件
    set eventignore=all
    " 恢复正常（清空事件忽略）
    set eventinnore=
```

### 3.6 非自动执行自动命令
在事件触发后执行一个自动命令。<br/>
***do[autocmd]***
```vim
    " 格式：doautocmd [nomodeline] [group] {event} [fname]
    " fname       默认为当前文件或者针对当前缓冲区
    " group       特定组或者所有组
    " nomodeline  应用完自动命令后，该选项用于过滤否则自动命令中的设置
    
    " 嵌套包含到自动命令au中（避免死循环）
    au BufEnter \*.cpp duau BufEnter x.c
```

***doautoa[ll]***
```vim
    " 为每个载入的缓冲区应用自动命令。用于执行类似于设置选项/修改高亮等任务
    " 的自动命令。
    " 格式：doautocmd [nomodeline] [group] {event} [fname]
```


## 4，vim会话管理
### 4.1 功能：
使用session和viminfo，保证当前环境，以便下次启动时进行现场恢复操作，类似Mysql的数据库迁移，记录各种命令
```txt
    session：所有窗口的视图、全局配置
    viminfo：各种历史命令、search操作、register/mark等等
```

### 4.2 会话和viminfo
#### 4.2.1 功能
本质：会话文件本质上是一个vim脚本，可以使用该文件(Session.vim)进行环境重建工作。  
viminfo：保存历史记录，因为每次会自动保存并覆盖~/.viminfo，所以必须手动建立一个

#### 4.2.2 保存
保存会话：mksession!  gcc.vim 或者 mk! gcc.vim  
加载保存的会话：source gcc.vim 或者 vim -S gcc.vim(建议）

#### 4.2.3 配置
不希望在session文件中保存当前路径，而是希望session文件所在的目录自动成为当前工作目录，
这样每次载入session件时，此文件所在的目录就被设为vim的当前工作目录。  
在你通过网络访问其它项目的session文件时，或者你的项目有多个不同版本（位于不同的目录）
```vim
    " session文件不保存当前路径，加载时将session所在目录设置为当前工作目录
    " 之后在网络访问其他项目的session或者多个不同目录的session时就蛮有用的
    set sessionoptions-=curdir
    set sessionoptions+=sesdir

    " 保存/读取session和viminfo
    map <silent> <leader> ex-mksession!<cr> ex-wviminfo
    map <silent> <leader> ex-source ./Session.vim<cr>
```

## 5 折叠语法
### 5.1 术语
```txt
    文档：http://vimcdoc.sourceforge.net/doc/fold.html
    术语:
        foldlevel          The foldlevel is computed from the indent of the line, divided by the shiftwidth.
        foldmethod          设置折叠的方式，见下面的命令介绍
```

### 5.2 命令
```vim
    "foldmethod折叠的方法（6种）:
    manual         " 手动设置
    indent         " 缩进来折叠
    syntax         " 语法来折叠
    expr           " 表达式定义来折叠
    marker         " 用标志折叠
    diff           " 对没有更改的文本进行折叠

    " close
    zm          " 关闭折叠
    zM          " 关闭所有折叠

    " create
    zf          " 创建折叠（marker模式）

    " open current
    zo          " 打开当前折叠
    zO          " 打开当前所有嵌套折叠

    " open all 
    zr          " Reduce(减少) folding: Add v:count1 to
    zR          " Open all folds. This sets 'foldlevel' to
    zn          " Fold none:reset 'foldenable'. All folds will
    zN          " Fold normal: All folds will be as they were

    " fold
    zc          " 折叠当前行
    zC          " Close all folds under the cursor recurisively.
    za          " When on a closed fold: open it
    zA          " When on a closed fold: open it recursively.
                " PS:注意和zr/zR的区别，后者用于整个文件
   
    " delete folds
    zd          " 删除折叠（manual和marker模式）
    zD          " 删除所有折叠
```

## 6 管理插件
### 6.1 pathogen
#### 6.1.1 功能介绍
* pathogen让每个插件占有一个单独的目录，解决了文件分散的问题。
* 安装完pathogen之后，只需要在~/.vim/目录下新建一个目录~/.vim/bundle/，并将要安装的所有插件放在~/.vim/bundle/目录下即可以使用。
* 如果要删除某个插件，只需要将~/.vim/bundle/目录下对应的插件目录删除即可。
* 如果想保持某个插件为最新版本，直接从插件的仓库checkout一份代码到bundle目录即可

#### 6.1.2 配置
```vim
    " 关闭文件检测
    filetype off

    " 指定runtime path，默认为~/.vim/bundle/，如果有偏差，进行更改
    execute pathogen#infect('stuff/{}')
    " 读取所有的帮助文档信息
    call pathogen#helptags()

    " 重新开启文件检测
    syntax on
    filetype plugin indent on
```

#### 6.1.3 pathogen和git
结合git和pathogen来进行vim配置的云部署，弥补pathogen无法安装插件、删除、更新等管理功能，当然这些功能在vundle中已经存在了。  
<font color="red">优势和特点:</font>
* 仅仅依赖git，符合unix美学，pathogen仅仅做加载，git做插件管理
* github包含所有的vim插件库
* 扯淡

**命令**
```bash
    # 初始化
    git init
    git remote add origin git@github.com:unlessbamboo/vim.git
    git pull origin master
    # 推送
    git add .
    git push origin master
    
    # 安装pathogen
    git submodule add https://github.com/tpope/vim-pathogen.git   bundle/vim-pathogen
    #     添加配置如下：
    #         " 指定pathogen的路径
    #         filetype off
    #         runtime bundle/vim-pathogen/autoload/pathogen.vim    
    #         execute pathogen#infect()
    #         syntax on
    #         filetype plugin indent on
    # 其他插件放入子模块中管理（git-submodule使用）
    git submodule add https://github.com/vim-scripts/bash-support.vim.git  bundle/bash-support
    
    ###########################基本操作############################
    # 克隆主项目并一次性拉取子模块
    git clone --recursive git@github.com:unlessbamboo/vim.git
    # 初始化子模块
    git submodule init 
    # 更新所有模块并检出
    git submodule update --init
    # 升级所有子模块
    git submodule foreach 'git checkout master && git pull'
    
    # 删除子模块
    # 1 手动删除：
    # 删除引用信息
    vim .gitmoudles
    vim .git/config
    # 删除插件
    rm -rf bundle/{scripts-name}
    # 删除缓存
    git rm --cached bundle/{scripts-name}
    # 提交更改
    git add.; git commit -m 'Delete a scripts'; git push origin master
    
    # 2 自动删除
    git rm bundle/{scripts-name}
    git rm --cached bundle/{scripts-name}
    rm -rf .git/modules/bundle/{scripts-name}


    # 删除版本控制下面的一些dirty数据（一些modified/untrack文件）
    # 1 回滚
    git submodule foreach git reset --hard
    # 2 过滤dirty目录，添加ignore=dirty
    vim .gitmodules
    git diff bundle
    # 3 命令行解决dirty
    git config -f .gitmoudules submodule.<path>.ignore untracked.
```

### 6.2 vundle
#### 6.2.1 功能
* 同时在.vimrc中跟踪和管理插件
* 安装特定格式的插件(a.k.a. scripts/bundle)
* 更新特定格式插件
* 通过插件名称搜索Vim scripts中的插件
* 清理未使用的插件
* 可以通过单一按键完成以上操作,详见interactive mode

#### 6.2.2 自动完成
* 管理已安装插件的runtime path
* 安装和更新后,重新生成帮助标签

#### 6.2.3 安装
```bash
    git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

#### 6.2.4 配置
```vim
    " 去除VI一致性,必须
    set nocompatible
    " 必须，类似pathogen             
    filetype off                  

    " 设置包括vundle和初始化相关的runtime path
    set rtp+=~/.vim/bundle/Vundle.vim
    " 启动，或者指定一个vundle安装插件的路径call vundle#begin('~/some/path/here')
    call vundle#begin()
    " 让vundle管理插件版本,必须
    Plugin 'VundleVim/Vundle.vim'


    " 使用不同格式来进行插件安装
    Plugin 'tpope/vim-fugitive'


    " 必须项，放在末尾
    call vundle#end()      
    " 必须 加载vim自带和插件相应的语法和文件类型相关脚本
    filetype plugin indent on

    " 简要帮助文档
    " :PluginList      - 列出所有已配置的插件
    " :PluginInstall    - 安装插件,追加 `!` 用以更新或使用 :PluginUpdate
    " :PluginSearch foo - 搜索 foo ; 追加 `!` 清除本地缓存
    " :PluginClean      - 清除未使用插件,需要确认; 追加 `!` 自动批准移除未使用插件
    " 安装vimrc中的插件：
    " vim中
    PluginInstall
    " shell命令行
    vim +PluginInstall +qall
```


## 7 基本插件
### 7.1 UI美观插件
参考：https://www.quora.com/How-do-I-enable-256-bit-colour-terminal-in-ubuntu   <br/>
更改终端的配色方案时必须保证：终端的配色方案+环境变量一起配置。环境变量：

- tput colors   -This will report how many colors your terminal is using.
- echo $TERM   -This will tell you what terminal you are using.
- echo $COLORTERM  -If you are using a gnome you should see gnome-terminal.

*颜色检查脚本*：
```txt

    PS：xshell中不支持

    1）配色方案
        i）molokai配色
            说明：没有什么好说的（^_^）
        ii）solarized配色
            说明：不知道为何，一直做不到官网的效果图
        iii）通用配置
            新增功能：函数名自定义颜色、结构体颜色、当前行的底色等等
        iv）powerline配置
            见《 powerline安装》或者http://www.unusebamboo.com/2016/08/03/ubuntu14-04-env/说明
```

### 7.2 nerdcomenter
**功能**：comment everything，soso.

**选项**:
```vim
    let leader = ","
    " Add spaces after comment delimiters by default
    let g:NERDSpaceDelims = 1
    " Use compact syntax for prettified multi-line comments
    let g:NERDCompactSexyComs = 1
    " Align line-wise comment delimiters flush left instead of following code indentation
    " 终于找到了，哇，果然英文版最好了
    let g:NERDDefaultAlign = 'left'
    " Set a language to use its alternate delimiters by default
    let g:NERDAltDelims_java = 1
    " Add your own custom formats or override the defaults
    " let g:NERDCustomDelimiters = { 'c': { 'left': '/**','right': '*/' } }
    " Allow commenting and inverting empty lines (useful when commenting a region)，注释空行
    let g:NERDCommentEmptyLines = 1
    " Enable trimming of trailing whitespace when uncommenting，自动修正结尾空格
    let g:NERDTrimTrailingWhitespace = 1

    " 添加注释
    <leader>cc
    " 取消注释
    <leader>cu
    " 性感的方式注释:  /* * */
    <leader>cs                   
    " 光标以下num行注释(包括当前行)
    num<leader>cc

    " Comments the given lines using only one set of multipart delimiters.
    num<leader>cm
    " 自动判断首行是否注释，如果注释则执行<leader>cu,否则执行<leader>cc
    num<leader>c<space>
    " Comments the current line from the cursor to the end of line
    <leader>c$
    " 先复制在注释，非常有用
    <leader>cy
    " 在可选的注释之间进行切换，例如/**/和//
    <leader>ca
```

### 7.3 Calendar
**功能**：
```txt
    基本日历
    时间表，事件的开始和结束，用于日程表
    任务列表，简单的Todo list
    Google Calendar/Task 集成
```

**基本按键**:
```txt
        来源：
        help Calendar-->Normal mode default mappings               
        开启：
           Calendar                             
        Event windows或者Task window视图                           
            E:切换到event窗口                                       
            T:切换到task窗口                                       
            D:删除或者完成task                                     
            L:清楚所有completed task                               
            U:Uncomplete the task，标示为未完成                     
        untiltiy:                                                   
            t: Go to today                                         
            Q: exit                                                 

        日历页的跳转（家里老日历的一页翻转，时间单位不同翻转就不同）
           w    <plug>(calendar_next)                               
           b    <plug>(calendar_prev)                               
           gg/G <plug>(calendar_first_line/calendar_last_line)
```

### 7.4 quickfix
**功能**： 将编译过程中的错误信息保存到制定的缓存中， vim利用这些信息跳转到源文件的位置，进行错误修改.

**命令**:
```vim
    " 查看make选项：set makeprg                                         
    " 按键介绍：                                                       
    cc          " 显示详细的错误信息，在vim状态栏中显示错误信息   
    cp          " 跳到上一个错误处，每一次都是显示cc的详细信息   
    cn          " 同cp相反                                       
    cw          " 如果存在错误列表，则打开一个窗口，默认行数为10 
    copen NUM   " 有时候和cw不同，比如ld错误的时候，cw没有任何信息
    cclose      " 关闭上面两个命令打开的窗口                     
    cnew        " 到后一个新的文件列表   
```

## 8 集散功能
### 8.1 正则例子
```vim
	" 将所有x%x替换为x % x，除了%s以及x % x以外
	"	说明：使用分组时，对()要使用破折符号
	%s/\([^ ]\)%\([^ s]\)/\1 % \2/g

	" 去掉文件中的所有^M换行符号
	" 其中^M 的输入：<C-v><C-m>生成；
	%s/^M//g

	" 将所有s1,s2的更改为s1,  s2
	%s/,\([^ ]\)/,  \1/g
```

### 8.2 tab and space
```vim
	" 将文档中的所有tab符号转为空格
	set tabstop=4
	set expandtab
	%ret!

	" 空格转tab键
	set ts=4
	set noexpandtab
	%retab!
```

### 8.3 缓冲区
```vim
	" 查看缓冲区
	ls
```

### 8.4 日期
```vim
	" 普通模式：nnoremap <F5> "=strftime("%F")<CR>gP
	" 插入模式：inoremap <F5> <C-R>=strftime("%F")<CR>
	" 会当前行的下一行打印日期
	r !date

    " 插入时间
    nnoremap <leader>date "=strftime("%Y-%m-%d %T")<CR>P
```

### 8.5 集散地
```vim
	" git中使用vim编写commit信息报错：SVN_EDITOR
	export SVN_EDITOR=vim
	" 关闭提示音
	visualbell

	" 错误fix
	lnext/lprev

	" 换行
	"使用'\'来进行换行，不同于其他语言，vimscript中将该符号放在每一行的前面
```


## 9 文档
### 9.1 search
```vim
    " F1或者help命令打开帮助文档
    help

    " 查看用户手册目录， TOC--tables of contents
    help user_toc

    " 查看特定命令的帮助信息
    help undo

    " 模糊查询，例如：逐一查询和插入模式相关的信息
    "   之后可以再quickfix窗口（clist, cnext, cprev, cwin, cclose）查看
    helpgrep insert mode

    " 查询快速索引
    help quickref

    " 查询vim使用技巧
    help tips
```

### 9.2 generate
```vim
    " 1 下载中文文档*.cnx到{runtime}/doc目录下

	" 2 生成帮助文档或者重新建立帮助索引
	helptags abspath-of-pugins/doc/

    " 设置vim使用的文档语言
    set helplang=cn
```

