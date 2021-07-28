/*
接口路由
*/
package router

import (
	"bambooweb/api/v1"
	"github.com/gin-gonic/gin"
)


func Http(router *gin.Engine) {
	apiRouter := router.Group("/api/v1")

	{
		/*
		1. 定义接口/api/v1/useradd, 处理函数UserAdd, 方法:
			POST: post方法
			GET: get
			ANY: get/post
		请求:
			curl --location --request POST 'http://127.0.0.1:8088/api/v1/useradd'
		*/
		apiRouter.POST("/useradd", v1.UserAdd)
	}
}