package helpers

import (
	"fmt"
	"strings"

	"bambooweb/conf"
	"bambooweb/library/database"

	"gorm.io/gorm"
)

/*
 初始化mysql:
	1. 创建连接并初始化
    2. 忽略测试数据库
*/
func InitMysql() {
    database.MysqlAllClients = make(map[string]*gorm.DB)
    for service, dbConf := range conf.BaseConf.Mysql {
        if strings.Contains(service, "test") {
            continue
        }
        dbConf.Service = service  // 服务名赋值
        if client, err := database.InitMysqlClient(dbConf); err != nil {
            panic("mysql connect " + service + " error :%s" + err.Error())
        } else {
            database.MysqlAllClients[service] = client
        }
    }
}


func InitTestMysql() {
    database.MysqlAllClients = make(map[string]*gorm.DB)
    for service, dbConf := range conf.BaseConf.Mysql {
        if !strings.Contains(service, "test") {
            fmt.Println("不符合要求的数据库连接服务:", service)
            continue
        }
        dbConf.Service = service  // 服务名赋值
        if client, err := database.InitMysqlClient(dbConf); err != nil {
            panic("mysql connect " + service + " error :%s" + err.Error())
        } else {
            database.MysqlAllClients[service] = client
        }
    }
}