/*
http错误处理
*/
package library

import (
	"encoding/json"
	"github.com/gin-gonic/gin"
	"net/http"
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
类方法: 填充数据
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