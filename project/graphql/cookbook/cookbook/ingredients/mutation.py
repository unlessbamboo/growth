# coding:utf8
import graphene

from cookbook.ingredients.models import Category, Ingredient

from .mutation_node import Episode
from .ingredient_node import IngredientNode


class EchoEpisode(graphene.Mutation):
    """如下查询:
        mutation{
          echoEpisode(enum: NEWHOPE) {
            description
          }
        }
    """
    class Input:
        enum = Episode()

    description = graphene.String(description='回显')

    @staticmethod
    def mutate(root, args, context, info):
        # 根据name获取EnumTypeMeta对象: Episode['name1']
        # 根据value获取EnumTypeMeta对象: Episode.get(value)
        value = Episode.get(args.get('enum')).description
        return EchoEpisode(value)


class CreateIngredient(graphene.Mutation):
    class Input:
        # InputFields and InputObjectTypes
        # 可以使用graphene.Argument()来封装下面的Fields
        name = graphene.String()
        notes = graphene.String()
        category_id = graphene.Int()

    output_ok = graphene.Boolean()
    output_ingredient = graphene.Field(lambda: IngredientNode)

    @staticmethod
    def mutate(root, args, context, info):
        category = Category.objects.get(id=args.get('category_id'))
        ingredient = Ingredient(name=args.get('name'), notes=args.get('notes', ''),
                                category=category)
        ingredient.save()
        output_ok = True
        return CreateIngredient(output_ingredient=ingredient, output_ok=output_ok)


class Mutation(graphene.ObjectType):
    echoEpisode = EchoEpisode.Field(description='回显episode')
    createIngredient = CreateIngredient.Field(description='创建ingredient')
