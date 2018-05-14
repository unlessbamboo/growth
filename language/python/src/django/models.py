# coding:utf8
"""
    django 中model操作
"""
from django.db import models


class AbstractImage(models.Model):
    """正常的django模型定义, 这里省略"""
    pass


# dynamic model Class
for i in range(1, 10):
    name = 'Image_{}'.format(i)

    class Meta:
        db_table = 'image_{}'.format(i)
        app_label = 'image'

    globals()[name] = type(name, (AbstractImage,), {
        '__module__': 'apps.image',
        '__unicode__': lambda self: 'Image Object: {}'.format(self.image_id),
        'Meta': Meta,
    })


# 利用__metaclass__来完成
def getModel(db_table):
    class ImageMetaClass(models.base.ModelBase):
        def __new__(cls, name, bases, attrs):
            name += db_table
            return models.base.ModelBase.__new__(cls, name, bases, attrs)

    class ImageClass(models.Model):
        __metaclass__ = ImageMetaClass

        class Meta:
            db_table = db_table

    return ImageClass
