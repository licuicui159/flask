from flask import Flask

app = Flask(__name__)

# http://localhost:5000
# http://localhost:5000/index
# http://localhost:5000/数字
# http://localhost:5000/index/数字
@app.route('/')
@app.route('/index')
@app.route('/<int:page>')
@app.route('/index/<int:page>')
def index(page=None):
    if page is None:
        page = 1
    return "您当前看的页数为:%d" % page

@app.route('/post',methods=['post'])
def post():
    return "这里只接收post请求"

if __name__ == "__main__":
    app.run(debug=True)