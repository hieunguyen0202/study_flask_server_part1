from flask import Flask, render_template, request
import os
app = Flask(__name__)
@app.route("/")
def home():
    users = [{
        "name" : "Nguyen Van A",
        "email" : "A@gmail.com"
    }, {
        "name" : "Tran Thi B",
        "email" : "B@gmail.com"
    }, {
        "name" : "Vo Van C",
        "email" : "C@gmail.com"
    }]

    kw = request.args.get("keyword")
    # nếu khác null
    if kw:
        kq = []
        for u in users:
            if u['name'].lower().find(kw.lower()) >= 0:
                kq.append(u)


        users = kq


    #  Cach viet code khac   users1 = [for u in users  if u['name'].find(kw) >= 0]
    return render_template("index.html", users1=users)


@app.route("/test")
def test():
    return "welcom toy"

## path param
# @app.route("/hello/<name>")
# def hello(name):
#     return render_template("index.html", massage="XIN CHAO %s !!! " % name)
## rang buoc du lieu
@app.route("/hello/<int:name>")
def hello(name):
    return render_template("index.html", massage="XIN CHAO %d !!! " % name)

# chao em yeu 123
##get param
@app.route("/hello2")
def hello2():
    # fn = request.args['first_name']
    # ln = request.args['last_name']
    fn = request.args.get('first_name', 'A')
    ln = request.args.get('last_name', 'B')
    return render_template("index.html", massage="WELCOME %s %s !!!" % (fn,ln))
# Cach khai bao duong dan phuong thuc get
# http://127.0.0.1:5000/hello2?first_name=Xuan&last_name=Hieu



# Tạo phương thức đăng nhập cho người dung

@app.route("/login", methods=['POST'] )
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == "123":
        return 'successful'
    else:
        return 'false'

@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['avatar']
    # Tạo đường dẫn
    file.save(os.path.join(app.root_path,'static/uploads/',file.filename))
    # file.save(app.root_path + '/static/uploads/' + file.filename)
    return 'done'


if __name__ == "__main__":
    app.run(debug=True)

