package main

import (
	"fmt"
	"time"
)


func showIndex(num int) {
	for i := 0; i<num; i+=1 {
		fmt.Println("Number:", i)
		time.Sleep(1 * time.Second)
	}
}

func main() {
	go showIndex(10)
	go showIndex(5)
	go showIndex(3)
	// 如果不等待, 主线程退出, 子线程也会退出
	fmt.Println("******************")
}