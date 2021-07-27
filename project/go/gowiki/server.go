package main

import (
	"fmt"
	"log"
	"net/http"
)


/*
@func: 定义请求处理回调函数
@return: 空
*/
func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Receive a new request...")
	fmt.Fprintf(w, "hi, there, i love %s!", r.URL.Path[1:])
}


func main() {
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":8083", nil))
}