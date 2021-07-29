package test
import (
    "fmt"
    "testing"
    "time"

    "bambooweb/library/cache"
)

/*
测试请求时间来判断是否存在缓存
*/
func TestRedis(t *testing.T)  {
    text := "上次请求时间为: "
    lastReqKey := "test:last:req:time"
    redisClient := cache.GetRedisClient()
    val, err := redisClient.Get(lastReqKey)
    if err != nil {
        t.Log(fmt.Sprintf("get from redis error. %#v", err.Error()))
    }
    text += val
    err = redisClient.Set(lastReqKey, time.Now().Unix(), 600 * time.Second)
    if err != nil {
        t.Log(fmt.Sprintf("set redis error. %#v", err.Error()))
    }
    t.Log(text)
}