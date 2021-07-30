package database

import (
    "fmt"
    "github.com/gin-gonic/gin"
    _ "github.com/go-sql-driver/mysql"
    "gorm.io/driver/mysql"
    "gorm.io/gorm"
    "time"
)


// mysql连接配置项
type MysqlConf struct {
    Service     string        `yaml:"service"`
    DataBase     string        `yaml:"database"`
    Addr         string        `yaml:"addr"`
    User         string        `yaml:"user"`
    Password     string        `yaml:"password"`
    MaxIdleConns int `yaml:"maxIdleConns"`
    MaxOpenConns int `yaml:"maxOpenConns"`
    ConnTimeout      time.Duration `yaml:"connTimeout"`
    ReadTimeout  time.Duration `yaml:"readTimeout"`
    WriteTimeout time.Duration `yaml:"writeTimeout"`
    ConnMaxLifeTime time.Duration `yaml:"ConnMaxLifeTime"`
}

// 2. 连接池(服务名 -> DB连接对象)
var MysqlAllClients map[string] *gorm.DB

/*
1. 根据配置生成连接URL
2. 打开数据库连接并生成连接对象指针: gorm.DB
*/
func InitMysqlClient(conf *MysqlConf) (client *gorm.DB, err error) {
	// a. mysql连接url
    fmt.Println("Mysql配置服务:", conf.Service, conf.User, conf.Password)
    dsn := fmt.Sprintf("%s:%s@tcp(%s)/%s?timeout=%s&readTimeout=%s&writeTimeout=%s&parseTime=True&loc=Asia%%2FShanghai",
        conf.User,
        conf.Password,
        conf.Addr,
        conf.DataBase,
        conf.ConnTimeout,
        conf.ReadTimeout,
        conf.WriteTimeout)

	// b. 打开mysql
    client, err = gorm.Open(mysql.Open(dsn), &gorm.Config{})
    if err != nil {
        return client, err
    }
    db, err := client.DB()
    if err != nil {
        return client, err
    }
    db.SetMaxOpenConns(conf.MaxOpenConns)
    db.SetMaxIdleConns(conf.MaxIdleConns)
    db.SetConnMaxLifetime(conf.ConnMaxLifeTime)
    return client, nil
}

// 3. DB 库信息
type DB struct {
    Name string
    Ctx *gin.Context
}

func (d *DB) GetConn() *gorm.DB {
    return MysqlAllClients[d.Name]
}

func NewDb(ctx *gin.Context, name string) DB {
    return DB{
        Name: name,
        Ctx: ctx,
    }
}