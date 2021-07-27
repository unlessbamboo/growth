package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

// 定义一个结构体
type Page struct {
	Title string
	Body []byte
}


/*
请求处理回调函数
*/
func viewHandler(w http.ResponseWriter, r *http.Request) {
	// 1. 截断URL, 获取view之后的title值
	title := r.URL.Path[len("/view"):]
	// 2. 提取文件中的值并打印输出
	p, err := loadPage(title)
	if err != nil {
		fmt.Printf("发生异常, 读取%s中的内容失败: %s", title, err)
	} else {
		fmt.Fprintf(w, "<h1>%s</h1><div>%s</div>", p.Title, p.Body)
	}
}


/*
定义结构体处理函数save: 将p.Body中的内容写入文件中
@receiver: Page指针
@parameters: 空
@return: error 或者 nil
*/
func (p *Page) save() error {
	filename := p.Title + ".txt"
	
	return ioutil.WriteFile(filename, p.Body, 0600)
}

/*
@func: 加载文件中的数据到结构体中, 其中伴随着结构体的实例化
@return: 返回Page指针, error
*/
func loadPage(title string) (*Page, error) {
	filename := "./" + title + ".txt"
	body, err := ioutil.ReadFile(filename)
	if err != nil {
		return nil, err
	}
	return &Page{Title: title, Body: body}, nil
}


func main() {
	// 1. 初始化结构体对象
	filetitle := "TestPage"
	p1 := &Page{Title: filetitle, Body: []byte("This is a simple Page.")}
	p1.save()
	// 2. 加载
	p2, _ := loadPage(filetitle)
	fmt.Println(string(p2.Body))

	// 3. 启动http server
	http.HandleFunc("/view/", viewHandler)
	log.Fatal(http.ListenAndServe(":8083", nil))
}