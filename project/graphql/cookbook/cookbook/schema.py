import graphene

from cookbook.ingredients.query import Query as MyQuery
from cookbook.ingredients.mutation import Mutation as MyMutation

from cookbook.ingredients.mutation_node import Episode


class Query(MyQuery, graphene.ObjectType):
    # 在root types(Query) 下定义resolver
    root = graphene.String(name=graphene.Argument(
        graphene.String, default_value="stranger"))

    episode_desc = graphene.String(description='返回一个枚举变量描述')

    def resolve_root(self, args, context, info):
        return 'Root Types resolver test case, echo: ' + args['name']

    def resolve_episode_desc(self, args, context, info):
        """每一个EnumTypeMeta有属性: description, name, value"""
        # 通过Episode[type]来获取EnumTypeMeta对象
        #  print(Episode['NEWHOPE'].value)
        return Episode.NEWHOPE.description


schema = graphene.Schema(query=Query, mutation=MyMutation)


# 保存完之后, 需要在前端触发一次调用
result = schema.execute(
    """
    query {
        episodeDesc
    }
    """)
print('Execute 调用, Data:', result.data, ' Error:', result.errors)
