/*
接口
*/
package v1

import (
	"fmt"
	// "io/ioutil"
	// "net/http"

	"github.com/gin-gonic/gin"

	"bambooweb/library"
	"bambooweb/services"
	"bambooweb/library/log"
)

/*
1. router/router.go中定义路由, 并设置该回调函数为请求处理函数
*/
func UserAdd(ctx *gin.Context) {
	// 1. 初始化ResponseBody实例对象
	rsp := library.NewResponseBody()
	// 2. 等待请求, 只有当前函数发生panic, defer标识函数中的recover才生效
	defer library.RecoverResponse(ctx, rsp)

	// panic("crash")  // 手动触发宕机操作
	// 3. 请求参数赋值并解析
	param := &services.UserRequestParams{Ctx: ctx}
	// BindJson问题:https://studygolang.com/articles/17745
	// err := ctx.BindJSON(param)  // 将请求参数绑定到param中: 规范接口参数类型, 进行接口参数检查
	err := ctx.ShouldBind(&param.User)
	if err != nil {
		msg := fmt.Sprintln("解析请求数据失败:", err.Error())
		log.Error(map[string]interface{}{}, msg)
		return
	}
	services.UserAdd(param, rsp)
}