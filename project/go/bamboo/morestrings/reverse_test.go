package morestrings

import (
	"testing"
)


func TestReverseRunes(t *testing.T) {
	// 1. 构造测试数据
	cases := []struct {
		in, want string  // 结构体存在两个字符串属性
	} {
		{"Hello, world", "dlrow ,olleH"},
		{"Hello, 世界", "界世 ,olleH"},
		{"", ""},
	}
	for _, c := range cases {
		got := ReverseRunes(c.in)  // 正串
		if got != c.want {
			t.Errorf("ReverseRunes(%q) == %q, want %q", c.in, got, c.want)
		}
	}
}