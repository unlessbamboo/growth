package main

import "fmt"

func main() {
  number := 9
  // 类似 C 的用法, 但是没有default
  switch number {
  case 5:
    fmt.Println("The number is 5")
  case 7:
    fmt.Println("The number is 7")
  case 10:
    fmt.Println("The number is 10")
  default:
    fmt.Println("The number is default:", number)
  }
}
