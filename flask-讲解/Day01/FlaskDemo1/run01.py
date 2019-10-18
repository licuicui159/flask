from flask import Flask

# 将当前运行的主程序构建成Flask应用，以便接收用户的请求(request)并给出响应(response)
app = Flask(__name__)

# @app.route() Flask中的路由定义，主要定义用户的访问路径。 '/' 表示的是整个网站的根路径
# def index()，表示的是匹配上@app.route()路径后的处理程序-视图函数。
# 所有的视图函数必须要有return，return后面可以是一个字符串也可以是一个独立的响应对象
@app.route('/')
def index():
    return "<h1>My First Flask Demo</h1>"

# 访问地址 http://localhost:5000/show/xxx
@app.route('/show/<name>')
def show(name):
    return "<h1>传递进来的参数为:%s</h1>" % name

#访问路径 http://localhost:5000/show/<name>/<age>
# @app.route('/show/<name>/<age>')
# def show_name_age(name,age):
#     return "<h1>姓名：%s,年龄:%s</h1>" % (name,age)

@app.route('/show/<name>/<int:age>')
def show_name_age(name,age):
    return "<h1>姓名：%s,年龄:%d</h1>" % (name,age)

@app.route('/category')
@app.route('/cate')
def category():
    return "<h1>商品分类页面</h1>"


if __name__ == "__main__":
    # 运行Flask应用(启动Flask服务)，默认在本机开启的端口是5000,port=5555,在指定端口启动程序
    #debug=True,将启动模式更改为调试模式(开发环境中推荐写 True , 生产环境中必须改成False)
    app.run(debug=True,port=5555)








