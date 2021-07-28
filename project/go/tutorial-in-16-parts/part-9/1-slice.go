package main

import "fmt"

func main() {
  languages := make([]string, 3)
  var newl [3] string
  languages[0] = "Go"
  languages[1] = "Ruby"
  languages[2] = "Pony"

  newl[0] = "zheng"
  newl[1] = "bifeng"
  newl[2] = "feng"

  fmt.Println(languages)
  fmt.Println(newl)
}
