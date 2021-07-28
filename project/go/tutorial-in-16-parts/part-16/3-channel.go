package main

import (
  "fmt"
  "time"
)

// 基于管道来实现多线程之间的数据共享服务
var webservice = make(chan int)

func callWebService() {
  go func() {
    fmt.Println("Calling webservice")
    time.Sleep(5 * time.Second)
    fmt.Println("Webservice Finished")
    webservice <-10  // 数据写入管道
  }()
}

func showToUser() {
  fmt.Println("Showing info to User..")
}

func main() {
  callWebService()

  showToUser()

  result := <-webservice  // 读取管道中数据

  fmt.Println("Execution finished with the result:", result)
  time.Sleep(8 * time.Second)
}
