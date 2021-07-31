package main

import (
	"github.com/gin-gonic/gin"
	// "net/http"
	"bambooweb/conf"
	"bambooweb/library/middleware"
	"bambooweb/router"
	// "bambooweb/library/log"
	"bambooweb/helpers"
)


func main() {
	// 1. 创建路由
	r := gin.Default()

	// 引入中间件
	r.Use(middleware.LoggerToFile())

	// 初始化配置
	conf.InitConf()
	helpers.InitMysql()
	// helpers.InitTestMysql()
	helpers.InitRedis()

	// 2. 绑定路由规则, 执行的函数(匿名函数)
	// r.GET("/", func(c *gin.Context) {
	// 	c.String(http.StatusOK, "Hello world")
	// })
	// 使用自定义路由绑定函数, gin.Context封装了request, response
	router.Http(r)

	// 3. 监听端口
	r.Run("0.0.0.0:8088")
}