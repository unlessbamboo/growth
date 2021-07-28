package main

import "fmt"

func main() {
  sumAndPrint(3, 6)
}

func sumAndPrint(first int, second float64) {
  sum := first + int(second)

  fmt.Println(sum)
}
