""" restful: endpoint-终点, API的具体网址.
flask_restplus: add_resource使用指定的endpoint注册路由到框架上(类似django路由中的name),
    如果没有指定endpoint, flask_restplus会根据类名自动生成.
"""
from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}


@api.route('/<string:todo_id>', endpoint='todo_ep_name')
class TodoSimple(Resource):
    def get(self, todo_id):
        # 三种返回方式: data, status_code, response headers
        return {todo_id: todos.get(todo_id, 0)}, 201

    def put(self, todo_id):
        # 从form表单中提取数据
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


@api.route('/hello', '/world')
class HelloWorld(Resource):
    def get(self):
        """ 返回最为简单的json格式 """
        return {'hello': 'world'}, 201, {'Content-Type': 'application/json'}


api.add_resource(HelloWorld, '/hello', '/world', endpoint='hello_ep_name')


if __name__ == '__main__':
    app.run(debug=True, port=5555)
