from flask import Flask
from flask_restplus import Resource, Api, Namespace

app = Flask(__name__)
# 1. 默认存在一个"default"的namespace: 为不同的资源, 不同的url进行分组.
# 2. 注意Api和Namespace的用法和不同之处
#   Api: The main entry point for the application, 其默认namespace为: default
#   Name
api = Api(app)
ns = Namespace('nsspace', description='重新定义一个新的命名空间')
# 只有将namespace加入到api之中后, 该namespace定义的接口才能在swagger中展示
api.add_namespace(ns)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        """ 返回最为简单的json格式 """
        return {'hello': 'world'}


@ns.route('/world')
class MyName(Resource):
    def get(self):
        return {'name': 'bifeng'}


if __name__ == '__main__':
    app.run(debug=True, port=5555)
