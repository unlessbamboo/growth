/* service: 接口业务处理层
route -> api -> services -> repositories -> models
*/
package services

import (
	"fmt"

	"github.com/gin-gonic/gin"

	"bambooweb/library"
	"bambooweb/library/log"
	"bambooweb/models"
	"bambooweb/repositories"
)

type user struct {
	Name string `form:"username" json:"username" xml:"username" uri:"username"`
	Password  string    `form:"password" json:"password" xml:"password" uri:"password"`
	Email  string    `form:"email" json:"email" xml:"email" uri:"email"`
}

// 请求参数
type UserRequestParams struct {
	Ctx *gin.Context
	User user
}

type UserService struct {
    userRepository *repositories.UserRepository
}

func NewUserService(ctx *gin.Context) *UserService {
    return &UserService{
        userRepository: repositories.NewUserRepository(ctx),
    }
}
func (s *UserService) Get(id int64) *models.User {
    return s.userRepository.Get(id)
}
func (s *UserService) Insert(username, password, email string) (int64, error) {
    return s.userRepository.Insert(&models.User{
        Username: username,
        Password: password,
        Email: email,
    })
}
func (s *UserService) Update(id int64, columns map[string]interface{}) error {
    return s.userRepository.Update(id, columns)
}
func (s *UserService) Delete(id int64) error {
    return s.userRepository.Delete(id)
}

// 接口: 添加用户(api/v1/user.go中被调用)
func UserAdd(param *UserRequestParams, rsp *library.ResponseBody) {
	// a. 实例化UserService(包含User Repository)
	user_service := NewUserService(param.Ctx)
	
	// b. 获取请求参数中的值
	fmt.Println("准备添加的新用户数据:", param.User)

	// c. 判断用户是否已存在
	old_user := user_service.userRepository.GetByName(param.User.Name)
	if old_user != nil {  // 表示用户已存在
		msg := fmt.Sprintf("用户:%s已存在, 添加用户失败", param.User.Name)
		log.Error(map[string]interface{}{}, msg)
		return
	}

	// d. 添加用户
	user := models.User{
		Username: param.User.Name,
		Password: param.User.Password,
		Email: param.User.Email,
	}
	uid, err := user_service.userRepository.Insert(&user)
	if err != nil {
		msg := fmt.Sprintf("用户:%s添加失败, 数据库操作失败", user.Username)
		log.Error(map[string]interface{}{}, msg)
		return
	}
	msg := fmt.Sprintf("用户:%s, email:%s添加成功, ID:%d, 恭喜", user.Username, user.Email, uid)
	log.Info(map[string]interface{}{}, msg)
}
