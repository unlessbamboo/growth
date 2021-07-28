package main

import "fmt"

func main() {
  printNumbers()
  printNumbers(1, 2, 3)
}

// 可变长数组
func printNumbers(numbers ...int) {
  fmt.Println(numbers)
}
