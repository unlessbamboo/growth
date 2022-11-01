"""
参数解析: 对请求数据进行校验, 以简化的代码进行参数检查, 避免硬编码和大量冗余代码存在.
    设计目的是对Flask中flask.request对象上的任何变量提供简单和统一的访问方式.
"""
from flask import Flask, request, jsonify, abort
from flask_restplus import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


tasks = [
    {
        'id': 1,
        'title': '标题1',
        'description': '标题描述',
        'done': 'done',
    }
]


@api.route('/todo/api/v1.0/tasks/<int:task_id>', endpoint='ParseS')
class ParseS(Resource):
    def put(self, task_id):
        """ 未使用参数检查的原始参数检查代码 """
        task = list(filter(lambda t: t['id'] == task_id, tasks))
        if len(task) == 0:
            print('1---------------')
            abort(404)
        if not request.json:
            print('2---------------')
            abort(400)
        if 'title' in request.json and not isinstance(
                request.json['title'], str):
            print('3---------------')
            abort(400)
        if 'description' in request.json and not isinstance(
                request.json['description'], str):
            print('4---------------')
            abort(400)
        if 'done' in request.json and not isinstance(
                request.json['done'], bool):
            print('5---------------')
            abort(400)
        task[0]['title'] = request.json.get('title', task[0]['title'])
        task[0]['description'] = request.json.get(
            'description', task[0]['description'])
        task[0]['done'] = request.json.get('done', task[0]['done'])
        return jsonify({'task': task[0]})


# 该功能在 2.0 之后被整体移除, 使用交互式的marsh来进行参数校验工作
# location表示从哪个位置获取值: form, args, headers, cookies, files, json
parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True,
                    help='任务描述', location='json')  # 请求中必须携带该参数
parser.add_argument('description', type=str, default="描述",
                    location='json')


@api.route('/todo/api/v2.0/tasks/<int:task_id>', endpoint='tasks')
class UserAPI(Resource):
    """ 增加参数检查校验工作 """

    def get(self, task_id):
        return {'desc': 'Get Method'}

    def put(self, task_id):
        parser.parse_args()  # 解析参数
        return {'desc': 'Put Method'}


if __name__ == '__main__':
    app.run(debug=True, port=5555)
