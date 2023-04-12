""" 非数据描述符测试 """

class NonDataDescriptor:

    def __get__(self, instance, owner):
        if instance is None:
            print('__get__(): Accessing y from the class', owner)
            return self

        print('__get__(): Accessing y from the object', instance)
        return 'Y from non-data descriptor'


class Bar:
    nony = NonDataDescriptor()


bar = Bar()


if __name__ == '__main__':
    # 1. bar中不存在nony属性的时候, 此时会走__get__逻辑
    print('-----------未覆盖属性-----------')
    print(bar.nony)
    print()
    
    # 2. 覆盖
    bar.nony = 'bifeng'
    print('-----------覆盖属性后-----------')
    print(bar.nony)
    print()
