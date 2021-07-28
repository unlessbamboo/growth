package mathexp

import (
	"fmt"
	"strconv"
	"math"
)


// 1. 定义一个"已导出"属性, 值为圆周率
var MyPi float64 = math.Pi
var myPi float64 = math.Pi


// 2. 定义一个两个字符串数字相加的函数
func StrAdd(x, y string) (int, error) {
	// a. 将字符串转为整型
	xi, err := strconv.Atoi(x)
	if err != nil {
		fmt.Printf("转化字符串%s为整型失败\n", x)
		return 0, err
	}
	yi, err := strconv.Atoi(x)
	if err != nil {
		fmt.Printf("转化字符串%s为整型失败\n", y)
		return 0, err
	}

	return xi + yi, nil
}