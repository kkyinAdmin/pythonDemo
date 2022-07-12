from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login')
def login():
    return '登录成功'


# 转换器
@app.route('/uid/<uid>')
def index(uid):
    return "id为：" + uid


# 多个指向
@app.route('/page1')
@app.route('/page2')
def page0():
    return "这是page0"


if __name__ == '__main__':
    app.run()
