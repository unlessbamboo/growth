" 1. 函数调用, 搜索当前文件, 从当前光标所处位置开始(好奇怪的函数)
" a. help function-list搜索所有内置函数说明
" b. 
"   字符串操作函数: help string-functions
"   列表处理函数: list-functions
"   字典处理函数: dict-functions
"   浮点数: float-functions
"   blob: blob-functions
"   变量: var-functions
"   光标和位置标记: cursor-functions    mark-functions
"   其他
let str1 = "Current Date: 2022-10-30"
echo "Search Date结果:" search("Date: ", "W")
echo "Search time结果:" search("Time: ", "W")

" 格式化打印
echo printf("%4d: %.30s", 2, "bifeng")


" 2. 自定义函数
def Min(num1: number, num2: number): number
    var smaller: number
    if num1 < num2
        smaller = num1
    else
        smaller = num2
    endif
    return smaller
enddef
def MinCondition(num1: number, num2: number): number
    return num1 < num2 ? num1 : num2
enddef
# 调用函数两种方式: 放到表达式中, 使用call调用, 不能单独调用函数, 会出错
echo "(2, 3)最小值: " Min(2, 3)

" 3. :function, 列出所有用户自定义的函数(包括插件)
"    :function Fun1, 查看函数
" 函数调用调试: verbose=12

" 4. 删除一个函数
execute "delfunction Min"
