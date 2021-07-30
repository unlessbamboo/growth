package conf

import (
	"gopkg.in/yaml.v3"
	"io/ioutil"

	"bambooweb/library/cache"  // library.log引用了conf包, 这里会导致相互引用吗?
	"bambooweb/library/database"
)

var BaseConf Config

type LogConf struct {  // 解析log下的配置项
	Dir string `yaml:"dir"`  // 解析配置获取日志目录
}

type Config struct {  // 解析yaml文件
	Log LogConf `yaml:"log"`  // 自动关联到LogConf
	Redis *cache.RedisConf `yaml:"redis"`  // 自动关联到library/cache/redis.go中的RedisConf并解析
	Mysql map[string]*database.MysqlConf `yaml:"mysql"`  // 类似redis
}

var ConfigFile = "./conf/config.yaml" 


/*
初始化配置
*/
func InitConf() {
	// 1. yamlFile仅仅在if, else if 中有作用域
	// 解析配置文件
	yamlFile, err := ioutil.ReadFile(ConfigFile) 
	if err != nil {
		panic("读取配置文件失败:" + err.Error())
	}
	
	// 2. 将配置文件中的值赋值给Config对象: BaseConf
	err = yaml.Unmarshal(yamlFile, &BaseConf)
	if err != nil {
		panic("解析配置文件失败:" + err.Error())
	}
}