from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def register():
    if request.method == "POST":
        a = request.form['name']
        b = request.form['number']
        c = request.form['english']
        with open('data.txt','w',encoding='utf-8')as f:
            f.write(a+'\n')
            f.write(b+'\n')
            f.write(c+'\n')
        return '成功接收到Post命令，并且对抓到的包进行保存'
    if request.method == "GET":
        number = ''
        with open('data.txt','r',encoding="utf-8")as f:
            content = f.readlines()
            for i in content:
                number += i
        return number

if __name__ == '__main__':
    app.run(debug=True)