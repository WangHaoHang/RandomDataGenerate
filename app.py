import datetime
import sys

from flask import Flask, request, make_response, jsonify, render_template, send_file, session, redirect, url_for
from service.random_text_service import random_stu_score_threshold_type, random_stu_score_threshold
from service.utils import save_csv
from model.result.resultMsg import resultMsg
from service.entity.user import User
from service.authority import insert_user, check_user
from service.translate.translate_service import TranslateService
import os


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

def get_username_passwd():
    '''
    获取用户名和密码1
    :return:
    '''
    name = request.cookies.get('User')
    passwd = request.cookies.get('Passwd')
    return name, passwd


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
    return redirect('/gendata.html')
    # return make_response(jsonify(rsp.__dict__))


@app.route(rule='/registername', methods=['GET'])
def register_name():
    name = request.args.get('name')
    passwd = request.args.get('passwd')
    insert_user(name, passwd)
    rsp = resultMsg()
    rsp.code = '0'
    return make_response(jsonify(rsp.__dict__))


@app.route(rule='/checkname', methods=['GET'])
def check_name():
    name = request.args.get('name')
    passwd = request.args.get('passwd')
    rsp = resultMsg()
    rsp.code = '0'
    if check_user(name, passwd):
        rsp.msg = 'success'
    else:
        rsp.msg = "fail"
    return make_response(jsonify(rsp.__dict__))


@app.route(rule='/register', methods=['GET', 'POST'])
def register():
    '''
    注册用户
    :return:
    '''
    name = request.json.get('username')
    passwd = request.json.get('passwd')
    user = User()
    id = user.get_next_id()
    user.id = id
    user.name = name
    user.password = passwd
    user.insert()

    rsp = resultMsg()
    rsp.code = '0'
    rsp.msg = '成功'
    return make_response(jsonify(rsp.__dict__))


@app.route(rule="/get_translate_file", methods=['POST'])
def get_translate_file():
    filename = request.json.get('filename')
    pagesize = request.json.get('page_size')
    pageindex = request.json.get('page_index')
    rsp = resultMsg()
    rsp.data = []
    translate_service = TranslateService()
    try:
        title, result = translate_service.get_translate_file(filename, pageindex, pagesize)
        rsp.data = {'title': title, 'data': result}
        rsp.code = 0
        rsp.msg = 'success'
    except Exception as e:
        rsp.code = -1
        rsp.msg = 'failed'
        print(e)
    return make_response(jsonify(rsp.__dict__))


@app.route(rule="/save_translate_file", methods=['POST'])
def save_translate_file():
    pass


@app.route(rule='/gendata.html', methods=['GET'])
def gendata():
    '''

    :return:
    '''
    rsp = make_response(render_template('gendata.html'))
    return rsp


@app.route(rule='/translate.html', methods=['GET'])
def translate_html():
    rsp = make_response(render_template('translate.html'))
    return rsp


@app.route(rule='/download/<id>/<file_name>', methods=['GET', 'POST'])
def download(id, file_name):
    '''
    下载文件
    :param id: 用户序号
    :param file_name: 文件名
    :return:
    '''
    return send_file(path_or_file='model/datas/tmp/' + id + '/' + file_name, mimetype='application/text')


@app.route(rule='/savefile/<name>', methods=['GET', 'POST'])
def savefile(name):
    '''
    保存数据到文件中
    :param name: 文件名
    :return:
    '''
    # 数据
    data = request.json
    # 判断文件夹存在
    if not os.path.exists('model/datas/tmp/1/'):
        # 创建文件夹
        os.mkdir('model/datas/tmp/1/')
    # 保存数据到文件
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
    上传文件
    :return:
    '''
    # 文件key
    files = request.files.keys()
    print(files)
    for file in files:
        f = request.files[file]
        # 保存文件
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
