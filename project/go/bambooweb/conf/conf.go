package conf

import (
	"gopkg.in/yaml.v3"
	"io/ioutil"
)

var BaseConf Config

type LogConf struct {  // 解析log下的配置项
	Dir string `yaml:"dir"`  // 解析配置获取日志目录
}

type Config struct {  // 解析yaml文件
	Log LogConf `yaml:"log"`
}


/*
初始化配置
*/
func InitConf() {
	confPath := "./conf/config.yaml"
	// 1. yamlFile仅仅在if, else if 中有作用域
	if yamlFile, err := ioutil.ReadFile(confPath); err != nil {
		panic("读取配置文件失败:" + err.Error())
	} else if err := yaml.Unmarshal(yamlFile, &BaseConf); err != nil {
		panic("解析配置文件失败:" + err.Error())
	}
}