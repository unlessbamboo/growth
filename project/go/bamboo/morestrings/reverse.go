package morestrings

import (
	"fmt"
)

/*
字符串反转函数, 另外, 大写开头的函数名可以被其他packages引用使用
*/
func ReverseRunes(s string) string {
	// a. 对于强解释语言, 除非是指针,否则不需要做非空判断
	if s == "" {
		fmt.Println("It is a empty string.")
		return s
	}
	r := []rune(s)
	// b. 使用二分算法
	for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}