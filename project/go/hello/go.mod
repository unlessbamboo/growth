module mygo.com/hello

go 1.16

require (
	golang.org/x/text v0.3.6 // indirect
	mygo.com/greetings v1.1.0
	rsc.io/quote v1.5.2
)

replace mygo.com/greetings => ../greetings

//  Modules: 相关go包集合, 源代码交换和版本控制单元, go会依赖该文件记录和解析模块依赖性.
//      项目目录下的子目录不需要init, 所有子目录依赖都会在go.mod中组织.
//  
//  GO111MODULE:
//      off:    不支持module功能, 寻找依赖包方式使用传统的vendor目录或者GOPATH模式
//      on:     使用modules, 不去GOPATH目录下寻找
//      auto:   自动根据当前目录情况来决定
//  
//  命令:
//      module:     指定包的名字或路径
//      require:    指定依赖项模块
//      replace:    替换依赖项模块
//      excluse:    忽略依赖项模块
//  
//  go.sum:
//      文件包含特定模块版本内容的预期加密哈希. 
//      go命令基于该文件确保模块的未来下载与第一次下载相同.
