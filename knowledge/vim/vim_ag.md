---
title: Ag(The Silver Searcher)  

date:  2016-10-06 23:00:00  

tags: vim   

---

欢迎来到狂想的个人实验室。  
github：[unlessbamboo](https://github.com/unlessbamboo)


## 1 Introduction
### 1.1 Introduction
Ag——A code search tools similar to ack, with a focus on speed.

vim.ag——This plugin allow you use ag from vim, and shows results on a split window.

### 1.2 Reference
[ag.vim](https://github.com/rking/ag.vim)
[the_silver_searcher](https://github.com/ggreer/the_silver_searcher)


## 2 Configure
### 2.1 Install
#### 2.1.1 Ubuntu
```shell
    # silversearcher
    sudo aptitude install silversearcher-ag
    # ag.vim
    cd ~/.vim/ && git submodule add https://github.com/rking/ag.vim bundle/ag.vim
```

#### 2.1.2 MacOS
```shell
    # silversearcher
    brew install the_silver_searcher
    # vim.ag
    cd ~/.vim/ && git submodule add https://github.com/rking/ag.vim bundle/ag.vim
```

### 2.2 Configure
``` vim
    " Custom ag name and path(If you install Ag with source code.)
    let g:ag_prg="<custom-ag-path-goes-here> --vimgrep"
    
    " Configure ag.vim to alwarys start searching from your project root instead of the cwd.
    let g:ag_working_path_mode="r"
```


## 3 Usage
Search recursively in some path for the special pattern.

### 3.1 Format
> Ag [options] {pattern} [{directory}]，命令行上的操作

- Ag —— like grep, 在当前目录快速搜索, 同时在quickfix窗口中列出所有匹配项
- AgAdd —— like grepadd, 不同于grep, 会将新的匹配项插入quickfix窗口后面
- LAg —— like lgrep, 不同于grep, 会将匹配项放在local-list中
- LAgAdd —— like lgrepadd, 将匹配项append到local-list后面

### 3.2 Gotchas
Other special character are handled in the same way, 处理特殊字符, 例如:
```vim
    Ag '\\\#define' foo to search for #define foo
```

### 3.3 Exapmle
> shell命令:ag的用法, 具体可以见ag的man文档
```shell
    # Find files containg "foo", and print the line matches in context
    ag foo

    # Find files containg "foo", but only list the filenames
    ag -l foo

    # Find files containg "foo" case-insensitively
    ag -i -o foo

    # 查找文件名包含"bar"中的"foo"字符串
    ag foo -G bar

    # regex match
    ag '^ba(r|z)$'

    # Find files with a name matching "foo"
    ag -g foo
```


## 4 Quick Windows
```shell
    e    to open file and close the quickfix window(暂时不生效)
    o    to open (same as enter, <er>同样效果)

    go   to preview file (open but maintain focus on ag.vim results)
    t    to open in new tab
    T    to open in new tab silently
    h    to open in horizontal split
    H    to open in horizontal split silently
    v    to open in vertical split
    gv   to open in vertical split silently
    q    to close the quickfix window
```
