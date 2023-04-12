"""
功能: 通过type(name, bases, dict)方式来创建新类并将该新类作为基类
"""
import datetime


class IntegerFiled(object):
    """IntegerFiled: 实现自定义的integer类"""

    def __init__(self, value, maxLength=4):
        """__init__

        :param value:
        :param maxLength:   整数最大位数
        """
        self.value = value[:maxLength]

    @property
    def value(self):
        """value"""
        return self.valu


def with_metaclass(meta, base=object):
    """with_metaclass:对metaclass的封装，并返回元类对象，不是实例哦

    :param meta: 某个cls类对象, 并且要求meta为type的子类, 否则无法使用下面的方法创建新类
    :param base: 父类
    """
    # 例如: ParentBase('NetMetaBase, (base,), {}), 其中ParentBase为type的子类
    return meta("NewMetaBase", (base, ), {})


class ParentBase(type):
    """ 注意, 因为其是type的子类, 所以使用type(name, base, dict)的方式创建新的类 """
    def __new__(mcs, name, base, attrb):
        """ 见metaclass_class.py中的type用法

        :param name: 类名称
        :param base: 基类的元祖, 例如: ()
        :param attrb: 命名空间变量字典, 例如: {'bar': True}
        """
        meta = attrb.pop("MetaV", None)
        newClass = super(ParentBase, mcs).__new__(mcs, name, base, attrb)
        newClass.now = getattr(meta, "curTime", None)  # 获取类中的属性并赋值
        return newClass


class Child(with_metaclass(ParentBase)):
    """Parent, 相当于：
        NewBase = ParentBase("NewMetaBase", (object,), {})
        class Parent(NewBase):
            pass
    亦等价于：
        class NewBase(object):
            __metaclass__ = ParentBase

        class Parent(NewBase):
            pass
    具体关于元类的解释见文档说明
    """
    class MetaV:
        curTime = datetime.datetime.now()


if __name__ == '__main__':
    print('-----------通过type创建新类并被Parent继承----------')
    cobj = Child()
    print(cobj.now)
