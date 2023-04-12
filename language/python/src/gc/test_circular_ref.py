import sys


class A:
    pass


def get_obj_ref(obj) -> None:
    """ 打印引用计数信息, 每次函数传参, 则引用都会加1

    :param obj: 对象
    :rtype: None
    """
    print(f'对象{id(obj)}的引用计数为: {sys.getrefcount(obj)}')
    print()


if __name__ == '__main__':
    # A(): 此时计数为1, firstobj = XX, 此时计数变为2, secondobj.to = firstobj, 此时计数变为3
    firstobj, secondobj = A(), A()
    firstobj.to, secondobj.to = secondobj, firstobj

    print('---' * 10)
    print(f'对象{id(firstobj)}的引用计数为: {sys.getrefcount(firstobj)}')
    print(f'对象{id(secondobj)}的引用计数为: {sys.getrefcount(secondobj)}')

    print('---' * 10)
    del firstobj
    print('删除firstobj对象之后再次查看secondobj的引用计数, 发现其引用计数并未减少')
    print(f'对象{id(secondobj)}的引用计数为: {sys.getrefcount(secondobj)}')
    print(f'对象中的子属性{id(secondobj.to)}的引用计数为: {sys.getrefcount(secondobj.to)}')

