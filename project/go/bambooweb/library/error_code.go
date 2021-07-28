/*
自由库-错误码
*/
package library


const(
	ErrnoSuccess = 0  // 成功
	ErrnoError = 1  // 失败
	ErrnoUnknown = 2  // 未知错误
)
var ErrNoToMsgMap = map[int32]string {  // 字典: int -> string
	ErrnoSuccess: "成功",
	ErrnoError: "错误",
	ErrnoUnknown: "未知",
}


func GetErrMsg(errNo int32) string {
	if errMsg, ok := ErrNoToMsgMap[errNo]; ok {  // 两个表达式, 判断条件为后者
		return errMsg
	}
	return "未符合预期的错误"
}