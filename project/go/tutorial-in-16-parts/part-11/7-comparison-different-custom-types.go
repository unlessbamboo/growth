package main

import "fmt"

type Minute int
type Hour int

func main() {
  minutes := Minute(70)
  hour := Hour(10)

  // 别名可以跟原有真类型进行比较, 但是下面该情况不可以
  if minutes > hour {
    fmt.Println("This will never be executed")
  }

}
