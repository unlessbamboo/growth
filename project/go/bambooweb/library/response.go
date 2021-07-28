/*
http错误处理
*/
package library

import (
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

// 1. 定义响应结构体
type ResponseBody struct {
	Errno int32 `json:"errno"`  // json解析: 状态码
	Msg string `json:"msg"` // 错误描述
	Data interface{} `json:"data"`  // 响应数据
}


/*
@func: 创建或初始化一个响应结构体对象
*/
func NewResponseBody() *ResponseBody {
	return &ResponseBody{
		Errno: ErrnoSuccess,
		Msg: GetErrMsg(ErrnoSuccess),
		Data: map[string]interface{}{},
	}
}


/* 
类方法: set
*/
func (res *ResponseBody) SetData(data interface{}) {
	res.Data = data
}
func (res *ResponseBody) SetErrNo(errNo int32) {
	res.Errno = errNo
}
func (res *ResponseBody) SetErrMsg(errMsg string) {
	res.Msg = errMsg
}


/*
异常处理函数: 设置接口返回值格式, 下面函数实际上就是对返回值进行格式判断, 确保返回json
*/
func RecoverResponse(ctx *gin.Context, rsp *ResponseBody) {
	// 1. panic终止其后执行的代码, 若存在defer列表, 则逆序执行
	// 2. recover:控制goroutine的packnicking行为, 捕获panic, 影响应用行为, 调用方式:
	//		a. defer函数中, 终止packnicking, 恢复正常代码
	//		b. 获取通过panic传递的error
	if err := recover(); err != nil {
		fmt.Println("函数发生宕机, 设置未知错误码")
		rsp.SetErrNo(ErrnoUnknown)  // 如果RecoverResponse发生异常, 则设置rsp
	}

	fmt.Println("开始构造返回值")
	resp, err := json.Marshal(rsp)
	if err != nil {
		ctx.Data(http.StatusOK, "application/json;charset=utf8",
			[]byte(`{"errno": 1, "msg": "unknown"}`))
	} else {
		ctx.Data(http.StatusOK, "application/json;charset=utf8", resp)
	}
	return
}