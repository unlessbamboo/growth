package main

import (
	"fmt"
	"reflect"
)


type BaseHandler interface {
	// Name string	 // 接口只有方法声明, 不能有数据字段
	ShowName() string  // 打印名字
	SetName(string) // 设置
}


type Dog struct {
	Hair string  // 毛发
	Name string	 // 默认值为空字符串
}

func (d Dog) ShowName() string {
	fmt.Printf(
		"This a Dog, his name:%s, hair:%s\n", d.Name, d.Hair)
	return d.Name
}

func (d *Dog) SetName(s string) {
	d.Name = s
}

func ShowBase(handler BaseHandler) {
	fmt.Println("对象类型:", reflect.TypeOf(handler))
	handler.ShowName()
}


func main() {
	// 1. 初始化 Dog 结构体
	dog := Dog{Hair: "red"}
	dog.ShowName()

	// 2. 设置名字
	dog.SetName("David")
	ShowBase(&dog)
}