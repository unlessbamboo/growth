package main

import "fmt"
import "reflect"

func main() {
  var number int = 10
  var price float64 = 15.10

  fmt.Println(number, price)

  price = float64(number)  // 需要做强制类型转换
  fmt.Println(price)
  fmt.Println(reflect.TypeOf(price))
}
