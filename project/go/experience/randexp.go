package main

import (
	"fmt"
	"math/rand"
	"math/cmplx"
	"time"
	"unusebamboo.top/randexp/mathexp"
)


func main() {
	// 1. 设置随机数种子
	for i := 0; i < 5; i++ {
		rand.Seed(time.Now().Unix())
		fmt.Println("伪随机数:", rand.Intn(10))
		time.Sleep(1000 * time.Millisecond)  // millisecond返回毫秒持续时间
	}

	// 2. 打印其他模块的属性
	fmt.Println("圆周率:", mathexp.MyPi)
	// fmt.Println("圆周率:", mathexp.myPi)  // myPi为未导出变量, 无法被编译

	// 3. 测试字符串相加
	x, y := "123458", "898989"
	xy, err := mathexp.StrAdd(x, y)
	if err == nil {
		fmt.Printf("串%s + %s = %d\n", x, y, xy)
	}

	// 4. 基本类型
	var (
		boolexp bool = true
		intexp int = -3
		int8exp int8 = 2
		int64exp int64 = 3
		uintexp uint = 5
		float32exp float32 = 3.2
		float64exp float64 = 3.23
		complex128exp complex128 = cmplx.Sqrt(-5 + 12i)
	)
	fmt.Println("布尔型bool: ", boolexp)
	fmt.Println("整型int: ", intexp)
	fmt.Println("整型int8: ", int8exp)
	fmt.Println("整型int64: ", int64exp)
	fmt.Println("无符号整型uint: ", uintexp)
	fmt.Println("浮点型float32: ", float32exp)
	fmt.Println("浮点型float64: ", float64exp)
	fmt.Println("复数complex128: ", complex128exp)
}