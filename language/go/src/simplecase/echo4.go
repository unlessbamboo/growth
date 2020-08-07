package main

import (
	"flag"
	"fmt"
	"strings"
)

var n = flag.Bool("n", false, "这是一个提示, 请输入布尔值")
var sep = flag.String("s", " ", "这是一个分割符")

func main() {
	flag.Parse()
	fmt.Print(strings.Join(flag.Args(), *sep))
	if *n != true {
		fmt.Println()
	}
}
