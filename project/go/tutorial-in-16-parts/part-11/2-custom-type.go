package main

import "fmt"

// 类似 C 的用法, 定义类型别名
type Language string

func main() {
  language := Language("Java")

  fmt.Println(language)
}
