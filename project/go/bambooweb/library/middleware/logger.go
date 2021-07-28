/*
log中间件: 自动的记录请求前后的一些信息, 便于日志追踪
*/
package middleware

import (
	"bytes"
	"io/ioutil"
	"time"


	"github.com/gin-gonic/gin"
	"bambooweb/library/log"
)

func LoggerToFile() gin.HandlerFunc {
	return func(ctx *gin.Context) {
		// 1. 开始时间
		start := time.Now()

		// 2. 请求报文
		var requestBody []byte
		if ctx.Request.Body != nil {
			var err error
			requestBody, err = ctx.GetRawData()
			if err != nil{
				log.Warn(map[string]interface{}{"err": err.Error(), "获取请求体失败"})
			}
			ctx.Request.Body = ioutil.NopCloser(bytes.NewBuffer(requestBody))
		}

		// 3. 处理请求
		ctx.Next()
		end := time.Now()

		// 4. 日志记录
		log.Info(map[string]interface{} {
			"statusCode": ctx.Writer.Status(),
			"cost": float64(end.Sub(start).Nanoseconds()/1e4) / 100.0,
			"clientIp": ctx.ClientIP(),
			"method": ctx.Request.Method,
			"uri": ctx.Request.RequestURI,
		})
	}
}