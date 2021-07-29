package log

import (
	"bambooweb/conf"
	"fmt"
	"os"
	"path"

	"github.com/sirupsen/logrus"
)


func init() {
	// 设置日志格式为json
	logrus.SetFormatter(&logrus.JSONFormatter{
		TimestampFormat: "2021-07-27 10:59:33",
	})
	logrus.SetReportCaller(true)
}

func Debug(fields logrus.Fields, args ...interface{}) {
	setOutPutFile(logrus.DebugLevel)
    logrus.WithFields(fields).Debug(args)
}
func Info(fields logrus.Fields, args ...interface{})  {
    setOutPutFile(logrus.InfoLevel)
    logrus.WithFields(fields).Info(args)
}

/*
1. logrus.Fields本身定义: map[string]interface{}, 这点请注意
2. args会记录到msg减值对应的列表中
*/
func Warn(fields logrus.Fields, args ...interface{})  {
    setOutPutFile(logrus.WarnLevel)
    logrus.WithFields(fields).Warn(args)
}
func Fatal(fields logrus.Fields, args ...interface{})  {
    setOutPutFile(logrus.FatalLevel)
    logrus.WithFields(fields).Fatal(args)
}
func Error(fields logrus.Fields, args ...interface{})  {
    setOutPutFile(logrus.ErrorLevel)
    logrus.WithFields(fields).Error(args)
}
func Panic(fields logrus.Fields, args ...interface{})  {
    setOutPutFile(logrus.PanicLevel)
    logrus.WithFields(fields).Panic(args)
}
func Trace(fields logrus.Fields, args ...interface{})  {
    setOutPutFile(logrus.TraceLevel)
    logrus.WithFields(fields).Trace(args)
}

func setOutPutFile(level logrus.Level) {
	// 1. 判断日志文件夹是否存在
	if _, err := os.Stat(conf.BaseConf.Log.Dir); os.IsNotExist(err) {
		err = os.MkdirAll(conf.BaseConf.Log.Dir, 0777)
		if err != nil {
			panic(fmt.Errorf("create log dir '%s' error: %s", conf.BaseConf.Log.Dir, err))
		}
	}

	// 2. 对不同等级日志进行判断
	name := ""
	switch level {
	case logrus.DebugLevel:
		name = "debug"
	case logrus.InfoLevel:
		name = "info"
	case logrus.WarnLevel:
		name = "warn"
	case logrus.FatalLevel:
		name = "fatal"
	case logrus.ErrorLevel:
		name = "error"
	case logrus.PanicLevel:
		name = "panic"
	case logrus.TraceLevel:
		name = "trace"
	default:
		panic(fmt.Errorf("invaild log level error %d", logrus.ErrorLevel))
	}
	// 设置不同等级的日志文件名
	fileName := path.Join(conf.BaseConf.Log.Dir, name + ".log")

	// 3. 记录日志
	var err error
	os.Stderr, err = os.OpenFile(fileName, os.O_APPEND|os.O_WRONLY|os.O_CREATE,0644)
	if err != nil {
		fmt.Printf("打开文件%s失败, 错误:%d", fileName, err)
	}
	logrus.SetOutput(os.Stderr)
	logrus.SetLevel(level)
	return
}