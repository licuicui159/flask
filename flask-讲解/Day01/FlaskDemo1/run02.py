from flask import Flask

app = Flask(__name__)

#http://localhost:5000/login
@app.route('/login')
def login():
    return "<h1>欢迎访问登录页面</h1>"

#http://localhost:5000/register
@app.route('/register')
def register():
    return "<h1>欢迎访问注册页面</h1>"

if __name__ == "__main__":
    app.run(debug=True)







