# coding:utf8
# cookbook/ingredients/schema.py
import graphene

from customs import XPaginator
from cookbook.connection import XDjangoFilterConnectionField
from cookbook.node import CustomNode
from cookbook.ingredients.models import Category, Ingredient

from .ingredient_node import (
    CategoryType, CategoryFilterType,
    IngredientType, IngredientFilterType)


class Query(graphene.AbstractType):
    """Root type through which all access begins"""
    category = graphene.Field(
        CategoryType, id=graphene.Int(), name=graphene.String(),
        bamboo=graphene.String())
    all_categories = graphene.List(CategoryType)

    # 可以自动通过id来查询category项
    filter_category = CustomNode.Field(CategoryFilterType)

    all_filter_categories = XDjangoFilterConnectionField(
        CategoryFilterType,
        page=graphene.Int())

    ingredient = graphene.Field(
        IngredientType, id=graphene.Int(), name=graphene.String())
    all_ingredients = graphene.List(
        IngredientType,
        page=graphene.Int(),
        page_size=graphene.Int())

    # 回归官方正版使用方法
    all_filter_ingredients = XDjangoFilterConnectionField(
        IngredientFilterType, description='所有的材料')

    def resolve_category(self, args, context, info):
        id = args.get('id')
        name = args.get('name')
        if id is not None:
            return Category.objects.get(pk=id)
        if name is not None:
            return Category.objects.get(name=name)
        return None

    def resolve_all_categories(self, args, context, info):
        return Category.objects.all()

    def resolve_all_filter_categories(self, args, context, info):
        """老版本, 有错误"""
        categories = Category.objects.all().order_by('-created')
        if 'page' in args:
            page = args.get('page', 0)
            if 'last' in args:
                page_size = args.get('last', 10000)
            else:
                page_size = args.get('first', 10000)

            categories = x_paginator_objs(categories, page, page_size)
        return categories

    def resolve_ingredient(self, args, context, info):
        id = args.get('id')
        name = args.get('name')
        if id is not None:
            return Ingredient.objects.get(pk=id)
        if name is not None:
            return Ingredient.objects.get(name=name)
        return None

    def resolve_all_ingredients(self, args, context, info):
        """page无法和过滤参数联合使用"""
        ingredients = Ingredient.objects.select_related(
            'category').all().order_by('-created')
        if 'page' in args:
            ingredients = x_paginator_objs(
                ingredients, args.get('page', 0), args.get('page_size', 10))
        return ingredients
