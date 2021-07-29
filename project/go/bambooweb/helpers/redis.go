/*
redis工具辅助函数
*/
package helpers

import (
	"github.com/gin-gonic/gin"

	"bambooweb/conf"
	"bambooweb/library/cache"
)

func InitRedis() {
	redisConf := conf.BaseConf.Redis  // 获取配置中解析redis配置
	cache.InitRedisClient(&gin.Context{}, redisConf)  // 初始化redis
}