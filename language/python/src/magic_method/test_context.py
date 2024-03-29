"""
功能: 上下文管理器协议, 涉及的魔术方法: __enter__, __exit__, 其指在一段代码执行之前执行一段代码，用于一些预处理工作, 执行之后再执行一段代码.

使用场景: 清理工作, 例如文件读写后文件的关闭, 数据库操作连接的关闭

with运行逻辑:
    with EXPR as VAR:
        BLOCK
    

参考: https://zhuanlan.zhihu.com/p/24709718
"""
