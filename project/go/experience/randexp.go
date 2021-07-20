package main

import (
	"fmt"
	"math/rand"
	"time"
)


func main() {
	// 1. 设置随机数种子
	rand.Seed(time.Now().Unix())
	fmt.Println("伪随机数:", rand.Intn(10))
	time.Sleep(1 * time.Microsecond)
}