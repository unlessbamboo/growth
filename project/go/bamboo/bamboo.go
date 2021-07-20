package main

import (
	"fmt"
	"unusebamboo.top/user/bamboohello/morestrings"  // 本地导入
	"github.com/google/go-cmp/cmp"  // 远程导入
)


func main() {
	fmt.Println("Hello, I am bamboo!")
	fmt.Println(morestrings.ReverseRunes("Hello, I will be reverse."))
	fmt.Println(cmp.Diff("字符串比较", "娃哈哈"))
}