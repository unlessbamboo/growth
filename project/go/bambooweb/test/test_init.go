/*
1. 测试用例初始化配置
*/
package test

import (
	"bambooweb/conf"
	"bambooweb/helpers"
)

func init() {
	conf.ConfigFile = "../conf/config.yaml"
	// 初始化配置
	conf.InitConf()
	helpers.InitRedis()
}