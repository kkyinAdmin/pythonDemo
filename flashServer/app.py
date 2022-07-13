from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 指定请求方式
@app.route('/login', methods=['POST', 'GET'])
def login():
    return '登录成功'


# 转换器
@app.route('/uid/<uid>')
def index(uid):
    # return "id为：" + uid
    return "id为：%s" % uid


# 多个指向
@app.route('/page1')
@app.route('/page2')
@app.route('/page3')
def page0():
    return "这是page0"


if __name__ == '__main__':
    # 调试 debug=True不生效     app.debug = True也不生效 app.config.update(DEBUG=True)也不生效 取决flask版本
    # app.debug = True
    # app.config.update(DEBUG=True)
    # 装饰器
    app.add_url_rule('/', 'urlRule', page0)
    app.run()
