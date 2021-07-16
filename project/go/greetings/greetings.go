package greetings

import (
    "fmt"
    "errors"
    "math/rand"
    "time"
)

// 定义一个Hello函数以便其他模块进行调用
func Hello(name string) (string, error) {
    // 1. 添加异常处理
    if name == "" {
        return "", errors.New("Empty Name")
    }

    // 2. 打印输出随机值
	message := fmt.Sprintf(randomFormat(), name)
	return message, nil
}


/*
功能: 传入一系列的名字, 返回一个字典
*/
func Hellos(names []string) (map[string]string, error) {
    // 1. 创建一个空map, 用于存储返回值
    messages := make(map[string]string)

    // 2. 遍历数组
    for _, name := range names {
        message, err := Hello(name)
        if err != nil {
            return nil, err
        }
        messages[name] = message
    }
    return messages, nil
}


// 初始化变量值, 设置一个随机数种子
// init函数先于main函数自动执行, 一个包可以有多个init函数, 执行顺序不一定
func init() {
    rand.Seed(time.Now().UnixNano())
}


// 返回一个随机格式化字符串
func randomFormat() string {
    // 1 定义一个字符串数组
    formats := []string {
        "Hi, %v. welcome!",
        "Great to see you, %v!",
        "Hail, %v! well met",
    }

    // 2. 随机返回
    return formats[rand.Intn(len(formats))]
}
