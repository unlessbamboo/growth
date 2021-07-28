package main

import "fmt"

func main() {
  i := 0
  // 类似python的while True:
  for {
    fmt.Println("Will break after this line!")
    i += 1
    if i > 10 {
      break
    }
  }
}
