""" 惰性取值和装饰器结合测试 """


CONFIG = {  # 假设这是上下文配置
}


class lazyproperty:
    """ 惰性属性
    @使用场景: 
        问题: 对于类中某个属性maxNum, 其依赖上下文配置中的某个配置MAX_NUM, 其中类的实例化在全局中进行,
            则在类进行实例化的时候上下文配置还未加载完全, 此时类的实例化就会报错
        解决: 通过懒加载的来将maxNum变为一个函数, 增加_maxNum变量来存储实际的值, 具体见下面的使用
    """

    def __init__(self, fun):
        self.fun = fun

    def __get__(self, instance, owner):
        """
        @描述符协议: 用来代理另外一个类的属性(代理模式)
            __get__: 调用一个属性时触发, 类似java中的getter
            __set__: 赋值一个属性时触发, 类似java中的setter
            __delete__: del删除时触发
        另见: 
            magic_method/test_property.py
            descripter/descripter_test.py

        参考: https://zhuanlan.zhihu.com/p/356076165
        """
        if instance is None:
            return self
        value = self.fun(instance)
        setattr(instance, self.fun.__name__, value)
        return value


class BambooPool:
    def __init__(self):
        self._maxnum = 0
        self._switch_queue = None

    @lazyproperty
    def maxnum(self):
        global CONFIG
        if self._maxnum > 0:
            return self._maxnum
        self._maxnum = CONFIG['MAX_NUM']  # 这里获取某个上下文配置中的值, 例如flask中的current_app.config配置
        return self._maxnum

    def show(self):
        print(f'当前最大数量: {self.maxnum}')


bamboo_pool = BambooPool()
try: # 未进行上下文初始化时调用就报错
    print('1. 未初始化时调用: ')
    bamboo_pool.show()
except Exception as msg:
    print('-------异常--------\n')


if __name__ == '__main__':
    # 初始化上下文配置
    CONFIG['MAX_NUM'] = 10
    print('2. 初始化上下文之后调用:')
    bamboo_pool.show()
    print('-------成功--------\n')
