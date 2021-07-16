/*
功能: greetings测试用例
*/
package greetings

import (
	"regexp"
	"testing"
)

// 1. 测试Hello返回指定格式的名字
func TestHelloName(t *testing.T) {
    name := "test1"
    want := regexp.MustCompile(`\b` + name + `\b`)

    // a. 判断返回值是否为希望的值
    msg, err := Hello(name)
    if !want.MatchString(msg) || err != nil {
        t.Fatalf(`Hello("Gladys") = %q, %v, want match for %#q, nil`, msg, err, want)
    }
}


// 2. 测试异常情况
func TestHelloEmpty(t *testing.T) {
    // a. 测试是否返回异常情况
    msg, err := Hello("")
    if msg != "" || err == nil {
        t.Fatalf(`Hello("") = %q, %v, want "", error`, msg, err)
    }
}
