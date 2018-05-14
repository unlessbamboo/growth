# coding:utf8
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
    """with_metaclass:对metaclass的封装，
        并返回元类对象，不是实例哦

    :param meta:
    :param base:
    """
    # type的__init__
    return meta("NewMetaBase", (base, ), {})


class ParentBase(type):
    """ParentBase"""
    def __new__(mcs, name, base, attrb):
        """__new__

        :param name:
        :param base:
        :param attrb:
        """
        meta = attrb.pop("MetaV", None)
        newClass = super(ParentBase, mcs).__new__(mcs, name, base, attrb)
        # 获取类中的属性并赋值
        newClass.now = getattr(meta, "curTime", None)
        return newClass


class Parent(with_metaclass(ParentBase)):
    """Parent
        相当于：
            NewBase = ParentBase("NewMetaBase", (object,), {})
            class Parent(NewBase):
                pass
        相当于：
            class NewBase(object):
                __metaclass__ = ParentBase

            class Parent(NewBase):
                pass
        具体关于元类的解释见文档说明
    """
    pass


class Child(Parent):
    class MetaV:
        curTime = datetime.datetime.now()


if __name__ == '__main__':
    cobj = Child()
    print cobj.now
