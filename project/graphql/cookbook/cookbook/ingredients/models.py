# coding:utf8

# cookbook/ingredients/models.py
from django.db import models


class DateTimeModel(models.Model):
    """ A base model with created and edited datetime fields """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(DateTimeModel):
    """种类"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'


class Ingredient(DateTimeModel):
    """材料"""
    name = models.CharField(max_length=100, unique=True)
    notes = models.TextField()
    # 材料--->种类, M<--->1的关系
    category = models.ForeignKey(Category, related_name='ingredients')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ingredient'
