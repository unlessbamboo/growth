"""
@api.expect()装饰器允许你指定所需的输入字段.
    它接受一个可选的布尔参数 validate, 指示负载(payload)是否需要被验证.
"""
from flask import Flask
from flask_restplus import Api, Resource, fields, reqparse
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='Test Expect',
          description='A simple Expect API',)

ns = api.namespace('expect', description='展示某一个namespace描述信息')

# model() 函数允许你将你的模型实例化并注册到你的 API 或者 命名空间（Namespace） 中
# 这些信息会在swagger中展示
todo = api.model('Todo', {
    'id': fields.Integer(readonly=True, description='Model:这是一个唯一标识符'),
    'task': fields.String(required=True, description='Model: 任务详情')
})

# 对输入的字段进行校验, 这些信息会在swagger中展示: Models->Request Models
request_model = api.model('Request models', {
    'name': fields.String(required=True),
    'id': fields.Integer(),
})
parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='校验参数rate, 不知道在哪里生效')


@ns.route('/')
class ExpectTest(Resource):
    # expect中valiate和属性中required都必须同时设置为 True, 这样才能校验是否存在
    @ns.expect(request_model, validate=True)
    @ns.marshal_with(todo)
    def post(self):
        print(api.payload)
        return {
            'id': 1,
            'task': 'task test',
        }

    @ns.expect(parser, validate=True)
    def get(self):
        return {
            'desc': '使用expect测试Request Parser',
        }


if __name__ == '__main__':
    app.run(debug=True, port=5000)
