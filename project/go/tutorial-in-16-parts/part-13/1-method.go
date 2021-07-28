package main

import (
  "fmt"
  "strings"
)

type Description string

/* 定义类方法, d相当于self */
func (d Description) Upper() string {
  return strings.ToUpper(string(d))
}

func (d Description) Lower() string {
  return strings.ToLower(string(d))
}

func main() {
  description := Description("My Go special description")
  upper := description.Upper()
  fmt.Println(upper)

  fmt.Println(description.Lower())
}
