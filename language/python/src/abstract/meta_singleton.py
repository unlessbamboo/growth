""" 使用meta创建单例, 通过__call__来完成单例模式的实例化, 每次调用Cls()都会调用__call__
"""

class SingletonMeta(type):
    """自定义单例元类"""

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            print('一个新的实例被创建')
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    pass


if __name__ == '__main__':
    print('---------第一次实例化---------')
    President()
    print()

    print('---------第2次实例化---------')
    President()
    President()
