package main

import "fmt"

func test() (i int, s string, e error) {
	return 0, "kuang", nil
}

func main() {
	fmt.Println("Hello, World!")
	fmt.Println(test())
}
