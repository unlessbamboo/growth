---
title: vim-surround and vim-repeat

date:  2016-10-09 19:00:00

tags: vim

---

欢迎来到狂想的个人实验室。  
github：[unlessbamboo](https://github.com/unlessbamboo)


## 1 Introduction
### 1.1 surround
surrround命令(s表示surround，周边)

### 1.2 repeat
重复一个插件的操作, 通过@:操作没办法做到.


## 2 Command
### 2.1 Normal Mode
- ds      delete a surrounding, 例如dst, 删除html
- cs      change a surrounding
- ys      add a surrounding，Not copy!
- yS      add a surrounding and place the surrounded text on a new line + indent it
- yss     add a surrounding to the whole line
- ySs     add a surrounding to the whole line, pleade it

### 2.3 Visual Mode
- s       add a surrounding, 不生效
- S       add a surrounding but place text on new line, 对所有行进行整体包括

### 2.4 Insert Mode
不会包括任何字符串，仅仅建立""：
- <c-g>s   add a surrounding
- <c-g>S   add a surrounding + new line + indent

### 2.5 内文本编辑
PS:Note the difference between ya and ys, after not copy

- ci/di/yi
- ca/da/ya
- cit/dit/yit(html)


## 3 HTML
### 3.1 修改元素节点
保留文本节点内容, 使用命令: cs + t + 替换值

### 3.2 修改文本节点
保留元素节点, 修改文本节点内容, 使用命令: ci + t + 输入 + ECS

### 3.3 添加元素节点
on a new line + indent it:
```
    ySS<div>:
        <div>
            source
        </div>
```


## 4 String
对某一个单词添加爽引号：
```vim
    Origin string:Hello wolrd
    Command or Key operate: ysw"
    Result string: "Hello" world
```

## 5 Repeat
### 5.1 Reference
来源见[vim-repeat](https://github.com/tpope/vim-repeat).

### 5.2 原理
实现下面的类似原理:
```vim
silent! call repeat#set("\<Plug>MyWonderfulMap", v:count)
```
