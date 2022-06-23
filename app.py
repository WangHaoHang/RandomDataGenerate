import datetime
import sys

from flask import Flask, request, make_response, jsonify, render_template, send_file, session, redirect

from service.random_text_service import random_stu_score_threshold_type, random_stu_score_threshold
from service.utils import save_csv
from model.result.resultMsg import resultMsg
import os

from werkzeug.security import generate_password_hash, check_password_hash

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

def get_username_passwd():
    '''

    :return:
    '''
    name = request.cookies.get('User')
    passwd = request.cookies.get('Passwd')


# @app.before_request
# def authenticate():
#     path_name = request.path
#     print('path', path_name)
#     # 1.获取cookie 没有跳转login.html
#     print('url:',request.url)
#     if request.path.endswith('login') or request.path.endswith('register') or request.path.startswith('/static/'):
#         pass
#     else:
#         name = request.cookies.get('RANDOMDATA_NAME')
#         if name is None:
#             return redirect('/login')


# test


# test
@app.route(rule='/randomdatas', methods=['POST'])
def random_datas():
    '''

    :return:
    '''
    result = resultMsg()
    req_data = request.json.get('subjects')
    req_num = request.json.get('nums')
    if req_data is None or len(req_data) == 0:
        result.error()
    else:
        data = random_stu_score_threshold_type(req_num, req_data)
        result.data = data
    resp = make_response(jsonify(result.__dict__))
    resp.headers['Content-Type'] = 'application/json'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'POST'
    return resp


@app.route(rule='/', methods=['GET', 'POST'])
def index():
    '''

    :return:
    '''
    resp = make_response(render_template('login.html'))
    return resp


@app.route(rule='/login', methods=['POST'])
def login():
    '''

    :return:
    '''
    name = request.json.get('username')
    passwd = request.json.get('passwd')
    rsp = resultMsg()
    print(name, passwd)
    from model.data_struct.user import User
    u = User.query.filter_by(name=name, password=passwd).first()
    if u is None:
        rsp.code = '-1'
        rsp.msg = '校验失败'
    else:
        return redirect('/gendata.html')
    return make_response(jsonify(rsp.__dict__))


@app.route(rule='/register', methods=['GET', 'POST'])
def register():
    '''

    :return:
    '''
    name = request.json.get('username')
    passwd = request.json.get('passwd')
    print(name, passwd)
    from model.data_struct.user import User
    u = User.query.order_by(User.id.desc()).first()
    user = User(id=str(int(u.id) + 1), name=name, password=passwd, ip_url=request.remote_addr)
    rsp = resultMsg()
    rsp.code = '0'
    rsp.msg = '成功'
    return make_response(jsonify(rsp.__dict__))


@app.route(rule='/gendata.html', methods=['GET'])
def gendata():
    '''

    :return:
    '''
    rsp = make_response(render_template('gendata.html'))
    return rsp


@app.route(rule='/download/<id>/<file_name>', methods=['GET', 'POST'])
def download(id, file_name):
    '''

    :param id:
    :param file_name:
    :return:
    '''
    return send_file(path_or_file='model/datas/tmp/' + id + '/' + file_name, mimetype='application/text')


@app.route(rule='/savefile/<name>', methods=['GET', 'POST'])
def savefile(name):
    '''

    :param name:
    :return:
    '''
    data = request.json
    if not os.path.exists('model/datas/tmp/1/'):
        os.mkdir('model/datas/tmp/1/')
    flag = save_csv('model/datas/tmp/1/' + name + '.csv', data)
    rsp = resultMsg()
    if flag:
        rsp.code = 0
        rsp.data = '/1/' + name + '.csv'
    else:
        rsp.code = -1
        rsp.msg = '失败'
    return make_response(jsonify(rsp.__dict__))


@app.route(rule='/text')
def text():
    '''

    :return:
    '''
    return make_response(render_template('text.html'))


@app.route(rule='/uploadfile', methods=['GET', 'POST'])
def uploadfile():
    '''

    :return:
    '''
    files = request.files.keys()
    print(files)
    for file in files:
        f = request.files[file]
        f.save('model/datas/tmp/' + f.filename)
    rsp = resultMsg()
    return make_response(jsonify(rsp.__dict__))


# test
@app.route(rule='/database', methods=['GET'])
def database():
    '''

    :return:
    '''
    # db.create_all()
    rsp = resultMsg()
    return make_response(jsonify(rsp.__dict__))


@app.route(rule='/getUser', methods=['GET'])
def getUser():
    '''

    :return:
    '''
    rsp = resultMsg()
    rsp.data = []
    from model.data_struct.user import User
    rows = User.query.all()
    for row in rows:
        rsp.data.append(row.name)
    return make_response(jsonify(rsp.__dict__))


# from service.authority import insert_user

if __name__ == '__main__':
    stu_info = random_stu_score_threshold(100, {'math': [50, 100], 'english': [10, 50]})
    print(stu_info)
    # print(insert_user())
    # from model.data_struct.user import User
    # print(User.query.order_by(name='id').first())
    app.run()
    print('hello  world!')
