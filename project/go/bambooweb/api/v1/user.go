/*
接口
*/
package v1

import (
	"bambooweb/library"
	"bambooweb/service"
	"fmt"
	// "net/http"

	"github.com/gin-gonic/gin"
)

/*
1. router/router.go中定义路由, 并设置该回调函数为请求处理函数
*/
func UserAdd(ctx *gin.Context) {
	// 1. 初始化ResponseBody实例对象
	rsp := library.NewResponseBody()
	// 2. 等待请求, 只有当前函数发生panic, defer标识函数中的recover才生效
	defer library.RecoverResponse(ctx, rsp)
	fmt.Println("准备解析请求参数")

	// panic("crash")  // 手动触发宕机操作
	// 3. 请求参数赋值并解析
	param := &service.UserRequestParams{Ctx: ctx}
	// BindJson问题:https://studygolang.com/articles/17745
	// err := ctx.BindJSON(param)  // 将请求参数绑定到param中: 规范接口参数类型, 进行接口参数检查
	err := ctx.ShouldBind(&param)
	if err != nil {
		fmt.Println("解析参数失败:", err)
		return
	}
	service.UserAdd(param, rsp)
}