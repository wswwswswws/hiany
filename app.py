from flask import Flask, render_template, request, jsonify
from sql import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_item', methods=['POST'])
def add_item():
    # 从请求中获取前端发送的数据
    data = request.json

    # 从数据中获取名称、图片和命名原因
    name = data.get('name')
    pic = data.get('pic')
    reason = data.get('reason')

    # 存入数据库
    insert({'name': name, 'pic': pic, 'reason': reason})

    # 返回响应给前端
    response = {'status': 'success', 'message': 'Item added successfully!'}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
