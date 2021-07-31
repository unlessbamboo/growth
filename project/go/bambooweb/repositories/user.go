/*
1 api请求数据: route -> api -> services -> repositories -> models
2. repositories(仓库): 相当于对model的封装, 提供各种小型的数据库数据处理函数: 增删改查
*/
package repositories
import (
    "time"

    "github.com/gin-gonic/gin"

    "bambooweb/library/database"
    "bambooweb/models"
)

// 数据库操作类
type UserRepository struct {
    database.DB  // API 连接数据库信息: name, ctx
    TableName string
}

// 实例化新的UserRepository对象(在services被使用)
func NewUserRepository(ctx *gin.Context) *UserRepository {
    return &UserRepository {  // 数据库表操作类
        database.NewDb(ctx, models.User{}.DatabaseName()),  // db对象
        models.User{}.TableName(),
    }
}

// 根据 ID 提取数据库中的User对象
func (r *UserRepository) Get(id int64) *models.User {
    ret := &models.User{}
    if err := r.GetConn().First(ret, "id = ?", id).Error; err != nil {
        return nil
    }
    return ret
}

func (r *UserRepository) GetByName(name string) *models.User {
    ret := &models.User{}
    if err := r.GetConn().First(ret, "username = ?", name).Error; err != nil {
        return nil
    }
    return ret
}

// 插入一个新的数据并返回新的记录 ID
func (r *UserRepository) Insert(u *models.User) (int64, error) {
    currTime := time.Now().Unix()
    u.UpdateAt = currTime
    u.CreateAt = currTime
    err := r.GetConn().Create(u).Error
    if err != nil {
        return 0, nil
    }
    return u.Id, err
}

// 更新
func (r *UserRepository) Update(id int64, columns map[string]interface{}) error {
    columns["update_at"] = time.Now().Unix()
    return r.GetConn().Model(&models.User{}).Where("id = ?", id).Updates(columns).Error
}

// 删除
func (r *UserRepository) Delete(id int64) error {
    return r.GetConn().Model(&models.User{}).Delete("id = ?", id).Error
}