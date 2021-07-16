package main

import (
    // 系统自带包
    "fmt"
    "log"

    // 第三方包
    "mygo.com/greetings"
)


// 调用第三方grettings中的函数
func main() {
    // 1. 记录日志格式
    log.SetPrefix("greetings:")
    log.SetFlags(1)  // 0: 关闭time, source file, line number的输出

    // 2. 测试异常情况
    var message string
    var err error
    if false {
        message, err = greetings.Hello("")
        if err != nil {
            log.Fatal("发生错误:", err)
        }
    }

    // 3. 测试正常情况
	fmt.Println("Hello world!");
    message, err = greetings.Hello("单人-A")
    if err != nil {
        log.Fatal("发生错误:", err)
    } else {
        fmt.Println(message)
    }

    // 4. 多人测试
    names := []string{"多人-1", "多人-2", "多人-3"}
    var messages map[string]string
    messages, err = greetings.Hellos(names)
    if err != nil {
        log.Fatal("发生错误:", err)
    }
    fmt.Println(messages)
}
