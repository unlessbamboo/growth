" vim变量和条件判断

" 1. 定义变量
let foo = "bar"
echo foo

" 2. 引用选项
set textwidth=80
echo &textwidth

" 3. 寄存器作为变量, 这执行source %, 此时A寄存器实际上保存了hello值
let @a = "hello"
echo @a

" 4. if, 注意非空串不是truthy, 但是对于以数字开头的会变为truethy
" 类似做了: int(str)
if "something"
    echom "one"
endif

" elseif, else
if 0
    echom "if"
elseif "nope"
    echom "elseif"
else
    echom "finally"
endif


" 5. for
let c = 0
for i in [1, 2, 3, 4]
    let c += i
endfor
echo "For 循环结果" c

" 6. while, 测试: source %
let c = 0
let total = 0
while c <= 4
    let total += c
    let c += 1
endwhile
echo "While 循环结果" total


" 数据结构-列表
let alist = ["app", "noot", "mies"]
call add(alist, "newvalue")
call extend(alist, ["l1", "l2"])
echo "列表值:"
for item in alist
    echo "\t" item
endfor

" 数据结构-字典
let adict = {"one": "een", "two": "twee", "three": "drie"}
echo "字典值:"
for key in sort(keys(adict))
    echo "\t" key ":" adict[key]
endfor
