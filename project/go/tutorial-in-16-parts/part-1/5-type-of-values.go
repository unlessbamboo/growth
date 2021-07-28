package main

import (
  "fmt"
  "reflect"  // 运行时态提取某一个对象的类型信息
)

func main() {
  fmt.Println(reflect.TypeOf(1))  // int
  fmt.Println(reflect.TypeOf(9.5))  // float64
  fmt.Println(reflect.TypeOf("Just a String"))  // string
  fmt.Println(reflect.TypeOf(true))  // bool
}
