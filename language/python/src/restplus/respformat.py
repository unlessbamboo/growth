"""
默认情况下: 返回的可迭代对象中的所有字段都会原样返回
响应编组(marlshaling): 类似django rest framework中的序列化, 利用
    fields和marshal_with进行自定义格式化输出, 以便处理数据库对象.
具体功能: 
    1. 重命名属性, 利用attribute来对外隐藏, 另外还可以访问嵌套属性
    2. 设置默认值, default
    3. 自定义, 继承fields.Raw, 实现
"""
import random
from flask import Flask
from flask_restplus import fields, Api, Resource, marshal_with, Model

app = Flask(__name__)
api = Api(app)


class UnreadItem(fields.Raw):
    """ 自定义格式输出 """

    def format(self, value):
        return "Unread" if value & 0x02 else "Read"


class RandomNumber(fields.Raw):
    """ 自定义随机数 """

    def output(self, key, obj, ordered=True):
        return random.random()


class RawOutput(fields.Raw):
    """ 原样输出 """

    def format(self, value):
        return value


# 响应参数校验工作: 
# 1. 校验返回值是否有效, 失败抛出flask_restplus.fields.MarshallingError:异常;
# 2. 过滤额外字段
# 3. 默认值: 不存在时返回默认值
sub_model = api.model('sub model', {
    'phone': fields.Integer(),
    'address': fields.String(),
})
friend_model = api.model('friend model', {
    'name': fields.String(),
    'age': fields.Integer(),
})
resp_model = api.model('resp model', {
    'task': fields.String(attribute='task_private'),  # 任务, 重命名属性来进行映射, 从而隐藏内在属性名
    # 会自动递归查找嵌套的属性, 直到找到所需属性, 必须确保返回值包含age_value
    'identify': fields.Integer(attribute=lambda x: x.age_value if hasattr(x, 'age_value') else 0),
    # Raw作为 BaseField基类, 一般用于自定义和未确定类型的字段(比例二维,三维, 思维数组等), 必须确保有该值, 否则异常
    'values': fields.Raw(),
    'raw': RawOutput(),  # 原样输出, 返回值可以不携带该属性
    'status': UnreadItem(attribute='flags'),  # flags字段值自动传入format函数中进行计算并返回
    'random': RandomNumber,

    'url': fields.Url('todo_ep', absolute=True),  # 接收一个端点名并返回该端点对应 URL
    'name': fields.String(default='bifeng'),  # 设置默认值

    'id': fields.Integer(),  # ID 测试
    'datetime': fields.DateTime(),  # 时间格式 
    'date': fields.Date(),  # 日期
    'bool': fields.Boolean(skip_none=True),  # 布尔型(可以在models或者expect中定义skip_none)

    'contact': fields.Nested(sub_model),  # 内嵌字典类型
    'friends': fields.List(fields.Nested(friend_model))  # 内嵌列表
})

person_model = api.clone('Person', resp_model, {  # clone继承(api方式继承)
    'weight': fields.Float(),  # 体重
})


m_model = Model('m model', {
    'name': fields.String,
    'address': fields.String,
})
c_model = m_model.clone('c model', {  # 这种方式和api.clone有一些不同
    'age': fields.Integer,
})


@marshal_with(c_model, skip_none=True)
def show_my():
    """ 自带的Model和marshal_with同api.Model, api.marshal_with的区别
    就是后者会自动添加到swagger文档中
    """
    return {'name': 'bifeng', 'address': 'hangzhou', 'age': 19}


@api.route('/todo/format', endpoint='todo_ep')
class TodoFormat(Resource):
    # 跳过返回 None的字段, 而不是返回null(该设置也可以在Nested中使用)
    @api.marshal_with(person_model, skip_none=True)
    def get(self):
        return {
            'task': 'format task',
            'id': 3,
            'desc': '冗余数据',
            'contact': {
                'phone': 158,
                'address': 'beijing',
            },
            'raw': [{}, 3],
            'values': {},
            'weight': 19.2,
        }


_task_model = api.model('', {
    'id': fields.Integer(),
    'task': fields.String(), 
})
# 继承语法, 注意使用(namespace也有inherit语法)
# orderer: 确保返回值的位置跟定义的位置保持一致, 这样会有一定的损耗.
# 该用法在: Api, Namespace, marsha1中都可以使用
order_model = api.inherit('order', _task_model, {
    'desc': fields.String(),
})


@api.route('/todo/order', endpoint='order_ep')
class TodoOrder(Resource):
    def get(self):
        # 利用order确保返回顺序和定义是一致的(和model中定义一致)
        v = {
            'id': 3,
            'task': 'format task',
            'desc': '冗余数据',
        }
        return api.marshal(v, order_model, ordered=True)


# 使用JSON 格式来定义模型, 注意, 下面方式只能用于expect和response
address_schema = api.schema_model('Address Schema', {
    'required': ['number', ],
    'properties': {
        'road': {
            'type': 'string'
        },
        'number': {
            'type': 'integer'
        },
        'country': {
            'type': 'string'
        }
    },
    'type': 'object'
})


@api.route('/todo/schema', endpoint='schema_ep')
class TodoSchema(Resource):
    @api.response(200, "ok", address_schema)
    def get(self):
        return {
            'country': '中国',
            'number': 110,
            'road': '余杭',
        }


if __name__ == '__main__':
    app.run(debug=True, port=5555)
