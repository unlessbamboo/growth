from graphene import relay


class CustomNode(relay.Node):
    class Meta:
        name = 'Node'

    @classmethod
    def to_global_id(cls, type, id):
        """返回的id值构造"""
        #  return '{}:{}'.format(type, id)
        return id

    @classmethod
    def get_node_from_global_id(cls, global_id, context, info, only_type=None):
        """设置获取node节点的id值方式"""
        return info.return_type.graphene_type._meta.model.objects.get(id=global_id)
