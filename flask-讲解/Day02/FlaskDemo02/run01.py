from flask import Flask, render_template

app = Flask(__name__)

class Person(object):
    name = None

    def say(self):
        return "hello im a person"

# 将 01-template.html 模板文件渲染成字符串再响应给客户端
@app.route('/01-template')
def template():
    # 将01-template.html渲染成字符串
   # return render_template('01-template.html')
   # 渲染01-template.html ，并传递变量

    # dic = {
    #     'music':'绿光',
    #     'author':'宝强',
    #     'qu':'乃亮',
    #     'singer':'羽凡',
    # }
    # return render_template('01-template.html',params=dic)

    music = '绿光'
    author = '宝强'
    qu = '乃亮'
    singer = '羽凡'

    #locals() : 将当前函数内所有的局部变量封装成一个字典
    print(locals())
    return render_template('01-template.html',params=locals())

#目的：能够传递到模板中作为变量的数据类型都有
@app.route('/02-var')
def var():
    uname = "my name is gebilaowang"
    bookName = '钢铁是怎样炼成的'
    author = '奥斯特罗夫斯基'
    price = 32.5
    list = ['漩涡鸣人','卡卡西','自来也','佐助']
    tup = ('水浒传','三国演义','红楼梦','西游记')
    dic = {
        'WMZ':'老魏',
        'WWC':'隔壁老王',
        'LZ':'吕泽',
        'MM':'蒙蒙',
    }
    person = Person()
    person.name = "狮王.金毛"
    print(locals())
    return render_template('02-var.html',params = locals())

#目的：练习变量和if标签
@app.route('/03-if')
def if_views():
    return render_template('03-if.html')

@app.route('/user/login')
def login():
    return "模拟登录的地址... ..."

@app.route('/04-for')
def for_views():
    list = ['孙悟空','猪八戒','周瑜','鲁班七号','孙尚香','大乔','沈梦溪']
    dic = {
        'SWK':'孙悟空',
        'PJL':'潘金莲',
        'XMQ':'西门庆',
        'WDL':'武大郎',
        'WWC':'王干娘',
    }
    return render_template('04-for.html',params = locals())

@app.route('/05-static')
def static_views():
    return render_template('05-static.html')

if __name__ == "__main__":
    app.run(debug=True)