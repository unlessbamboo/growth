package main

import "fmt"

type Language string

func main() {
  language := Language("Java")

  fmt.Println("Language:", language)

  print(string(language))
}

/* 虽然Language是string的别名, 但是两者术语不同的类型, 编译不通过 */
func print(value string) {
  fmt.Println("Value:", value)
}
