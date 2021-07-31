/*
接口请求数据逻辑顺序: route -> api -> services -> repositories -> models
*/
package models

// 定义数据库到结构体的映射: json, gorm, 表示既可以使用gorm对象转为User, 也可以使用json来转化
type User struct {
    Id int64 `json:"id" gorm:"primary_key;column:id"`
    Username string `json:"username" gorm:"column:username"`
    Password string `json:"password" gorm:"column:password"`
    Email    string `json:"email" gorm:"column:email"`
    UpdateAt int64 `json:"update_at" gorm:"column:update_at"`
    CreateAt int64 `json:"create_at" gorm:"column:create_at"`
}

func (u User) DatabaseName() string {
	// 写死, 返回一个固定的数据库名, 用于外面数据库对象的获取, 数据库操作类的初始化
    return "bambooweb"
}
func (u User) TableName() string {
    return "user"
}
func (u User) PrimaryKey() string {
    return "id"
}