from flask import Flask
from flask_restplus import Api, Resource, fields, reqparse
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='TodoMVC API', description='A simple TodoMVC API',)
parser = reqparse.RequestParser()

ns = api.namespace('todos', description='展示某一个namespace描述信息')

# 会在swagger中的model中展示相关信息
# model() 函数允许你将你的模型实例化并注册到你的 API 或者 命名空间（Namespace） 中
todo = api.model('Todo', {
    'id': fields.Integer(readonly=True, description='Model:这是一个唯一标识符'),
    'task': fields.String(required=True, description='Model: 任务详情')
})
parser.add_argument('rate', type=int, help='校验参数rate, 不知道在哪里生效')
#  args = parser.parse_args()


class TodoDAO():
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                return todo
        api.abort(404, "Todo {} doesn't exist".format(id))

    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)


DAO = TodoDAO()
DAO.create({'task': 'Build an API'})
DAO.create({'task': '?????'})
DAO.create({'task': 'profit!'})


@ns.route('/')
class TodoList(Resource):
    """Shows a list of all todos, and lets you POST to add new tasks"""
    @ns.doc('list_todos')
    @ns.marshal_list_with(todo)
    def get(self):
        """List all tasks"""
        return DAO.todos

    @ns.doc('create_todo')
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        """Create a new task"""
        return DAO.create(api.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Todo(Resource):
    """Show a single todo item and lets you delete them"""
    @ns.doc('get_todo')
    @ns.marshal_with(todo)
    def get(self, id):
        """Fetch a given resource"""
        return DAO.get(id)

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        """Delete a task given its identifier"""
        DAO.delete(id)
        return '', 204

    @ns.expect(todo)
    @ns.marshal_with(todo)
    def put(self, id):
        """Update a task given its identifier"""
        return DAO.update(id, api.payload)


@app.cli.command('list_route')
def list_route():
    print('以下是所有路由设置:')
    for route in app.url_map.iter_rules():
        print(route)
    print('*' * 10)


if __name__ == '__main__':
    app.run(debug=True, port=5555)
