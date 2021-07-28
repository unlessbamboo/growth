package main
// concurrency: 一致, 协调, routine: 常规, 一套动作

import (
  "fmt"
  "time"
)

func callWebService(value int) {
  fmt.Println("WebService started:", value)
  time.Sleep(3 * time.Second)
  fmt.Println("WebService finished:", value)
}

func main() {
  // 使用go开启goroutine, 轻量级线程, 有 Golang运行时管理
  go callWebService(1)
  go callWebService(2)
  go callWebService(3)
  time.Sleep(10 * time.Second)
}
