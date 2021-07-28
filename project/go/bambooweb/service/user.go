/* service: 接口业务处理层
*/
package service

import (
	"bambooweb/library"	
	"github.com/gin-gonic/gin"
)


// 请求参数
type UserRequestParams struct {
	Ctx *gin.Context
}


func UserAdd(param *UserRequestParams, rsp *library.ResponseBody) {
	return
}