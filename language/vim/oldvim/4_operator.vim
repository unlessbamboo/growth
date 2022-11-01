" 1. 逻辑操作符: ==, !=, >, >=, <, <=

" a. 返回结果: 1, ==?表示忽略大小写
echo "逻辑==:" "80" == 80
echo "逻辑!=:" "70" != 80
echo "逻辑>:" 90 > 80


" 2. 匹配模式: str =~ pattern
let str = "bamboo test"
if str =~ " "
    echo "字符串包含空格"
endif
" ^, $
if str !~ "\.$"
    echo "字符串不以句号结尾"
endif
