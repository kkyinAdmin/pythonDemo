from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login')
def login():
    return '登录成功'


# 转换器
@app.route('/index/<uid>')
def index(uid):
    return "id为：" + uid


if __name__ == '__main__':
    app.run()
