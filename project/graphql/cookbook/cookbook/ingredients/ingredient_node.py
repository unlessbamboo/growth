import graphene

from graphene_django.types import DjangoObjectType

from cookbook.connection import connection_for_type
from cookbook.ingredients.models import Category, Ingredient
from cookbook.node import CustomNode


class CategoryIngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        description = '材料-->关联-->种类'


class CategoryType(DjangoObjectType):
    """种类:Define object types"""
    ingredients = graphene.List(CategoryIngredientType)    

    class Meta:
        model = Category

    def resolve_ingredients(self, args, context, info):
        """通过手动的设置该边, 来避免自动的连接IngredientFilterType类型"""
        return Ingredient.objects.filter(category=self)


class CategoryFilterType(DjangoObjectType):
    """种类, 在filter中的用法"""
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (CustomNode, )


CategoryFilterType.Connection = connection_for_type(CategoryFilterType)


class IngredientType(DjangoObjectType):
    """食品，材料"""
    category = graphene.Field(
        CategoryType,
        description='手动指定, 不然会默认关联CatetoryFilterType类型')

    class Meta:
        model = Ingredient

    def resolve_category(self, args, context, info):
        """对于forgienkey, 使用该方式即可"""
        return self.category


class IngredientFilterType(DjangoObjectType):
    """食品，材料"""
    class Meta:
        model = Ingredient
        filter_fields = {
            # 例如name_Icontains: "e"
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            # 例如: category_Name: "meat"
            'category__name': ['exact'],
        }
        interfaces = (CustomNode, )


IngredientFilterType.Connection = connection_for_type(IngredientFilterType)


class IngredientNode(graphene.ObjectType):
    name = graphene.String()
    notes = graphene.String()
    category = graphene.Field(lambda: CategoryType)
