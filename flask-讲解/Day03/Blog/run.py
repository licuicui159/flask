from flask import Flask, render_template

app = Flask(__name__)

# 访问路径 http://localhsot:5000/
@app.route('/')
def index():
    return render_template('index.html')

#访问路径　http://localhost:5000/list
@app.route('/list')
def list():
    return render_template('list.html')

if __name__ == "__main__":
    app.run(debug=True)