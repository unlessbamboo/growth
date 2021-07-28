package main

import "fmt"

func main() {
  /*
    1.  注意map和make的用法区别
      make(t Type, size ... IntegerType) Type : 分配和初始化, 类似new语法
      map [key type] valueType {}: 创建字典类型
  */
  languages := map[string]int{}
  languages["java"] = 5
  languages["ruby"] = 4
  languages["go"] = 2
  fmt.Println(languages)

  mapLanguages := make(map[string]int)
  mapLanguages["name"] = 1
  fmt.Println(mapLanguages)
}
