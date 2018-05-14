import graphene
from graphene_django.filter import DjangoFilterConnectionField


def connection_for_type(_type):
    class Connection(graphene.Connection):
        count = graphene.Int()
        page = graphene.Int()
        page_size = graphene.Int()
        pages = graphene.Int()

        class Meta:
            name = _type._meta.name + 'Connection'
            node = _type

        class Edge:
            test = graphene.String()

        def resolve_count(self, args, context, info):
            return self.length

        def resolve_page(self, args, context, info):
            return self.page

        def resolve_page_size(self, args, context, info):
            return self.page_size

        def resolve_pages(self, args, context, info):
            return self.pages

    return Connection


class XDjangoFilterConnectionField(DjangoFilterConnectionField):
    """
    考虑到 Graphql 本身的输出不确定性, 所以无法使用Pagination类来进行传统分页.
    故, 创建了该函数, 但是有一个重大缺陷:
        page 无法和DjangoFilter提供的过滤参数一起使用.
    例如:
        page: 0, 过滤条件: name__icontains='e'
        实际上传递过来的是所有对象的第一页, 此时再进行过滤, 结果完全不同
    """
    @classmethod
    def connection_resolver(cls, resolver, connection, default_manager, max_limit,
                            enforce_first_or_last, filterset_class, filtering_args,
                            root, args, context, info):
        connection = super(XDjangoFilterConnectionField, cls).connection_resolver(
            resolver, connection, default_manager, max_limit,
            enforce_first_or_last, filterset_class, filtering_args,
            root, args, context, info)

        if 'first' in args:
            page_size = args.get('first')
        elif 'last' in args:
            page_size = args.get('last')
        else:
            page_size = connection.length
        page = args.get('page', 0)
        if page * page_size >= connection.length:
            page = page - (page * page_size - connection.length) // page_size - 1
        print(page, page_size, connection.length)

        connection.length = connection.length + page_size * page
        setattr(connection, 'page_size', page_size)
        setattr(connection, 'page', page)
        setattr(connection, 'page', page)
        if connection.length == connection.page_size:
            setattr(connection, 'pages', 1)
        else:
            setattr(connection, 'pages', connection.length / connection.page_size)

        return connection
