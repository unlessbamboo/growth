" 基本命令: source %

" 1. 输出
"   echo: 输出表达式内容
"   echom(echomsg): 输出表达式经过计算后的回显信息, 但是该信息会保存到messageshistory中
echo "Hello, World"
" . 表示连接两个字符串
echo "Hello" . "world"

" 换行(老版本, 新版本不需要)
let mylist = [
    \ "one",
    \ "two"]
echo "换行列表:" mylist

" 2. 选项-布尔值: on, off
set nonumber
set number
" " 两次调用, 回滚到之前的选项值
set number!
set number!
" " 获取当前选项值
set number?

" 3. 选项-非布尔值
" set numberwidth=10  " 行号的列宽
" set numberwidth?


" 4. 自动命令, 对指定文件进行文本缩进处理: :normal gg=G
" normal: 该命令后面跟着字符, 执行时类似在常用模式下的敲击
" 事件: BufWritePre -- 保存任何字符到文件之前时触发
autocmd BufWritePre *.html :normal gg=G
" 编辑HTML文件时关闭自动换行
autocmd BufNewFile,BufRead *.html setlocal nowrap


" 5. 自动命令组: 在执行完source %之后, 保存时候会输出
" 命令: messages(消息总览: help messages)会列出所有的历史输出信息
augroup testgroup
    " 清理自动命令组
    autocmd!
    autocmd BufWrite * :echom "Bar"
augroup END


" 6. execute 命令字符串: 将字符串当成vimscript命令执行, 用于解决normal不识别特殊字符的问题
"   该命令类似eval命令
execute "normal! gg"
execute "echom 'hello world'"
" 配合函数, 最终结果: rightbelow vsplit filename
execute "rightbelow vsplit " . bufname("#")
echom "rightbelow vsplit " . bufname("#")


" 7. normal 命令行命令
"   normal!: 类似nmap和nnoremap关系
