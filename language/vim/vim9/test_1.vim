vim9script
# 简单测试: a. 循环, b. 变量定义, c. 输出
# 测试命令: source %

# 1. while循环
echo "while循环测试:"
var i = 1
while i < 5
    echo "count is " i
    i += 1
endwhile


# 2. for
def FuncFor()
    echo "for循环测试"
    for i in range(1, 4)
        echo "count is " i
    endfor
enddef
FuncFor()
