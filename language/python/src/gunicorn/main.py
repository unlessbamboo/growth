""" flask 基本服务 """
import time

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/sleep")
def sleeptest():
    time.sleep(0.2)
    return "Block Test"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
