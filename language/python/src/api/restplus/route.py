""" 资源路由测试
resource: flask restplus提供的主要对象, 其创建于Flask可插入视图, 类似django restframework的viewset.
"""
from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)


todos = {}


@api.route('/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        # 三种返回方式: data, status_code, response headers
        return {todo_id: todos.get(todo_id, 0)}, 201

    def put(self, todo_id):
        # 从form表单中提取数据
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


if __name__ == '__main__':
    app.run(debug=True, port=5555)
