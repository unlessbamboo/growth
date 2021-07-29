package helpers

import (
    "bambooweb/conf"
    "bambooweb/library/database"
    "gorm.io/gorm"
)

/*
 初始化mysql: 
	1. 创建连接并初始化
 */
func InitMysql() {
    database.MysqlAllClients = make(map[string]*gorm.DB)
    for service, dbConf := range conf.BaseConf.Mysql {
        if client, err := database.InitMysqlClient(dbConf); err != nil {
            panic("mysql connect " + service + " error :%s" + err.Error())
        } else {
            database.MysqlAllClients[service] = client
        }
    }
}