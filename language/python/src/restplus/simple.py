from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
# 1. 默认存在一个"default"的namespace: 为不同的资源, 不同的url进行分组.
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        """ 返回最为简单的json格式 """
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True, port=5555)
