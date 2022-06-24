from werkzeug.security import generate_password_hash, check_password_hash
from service.random_text_service import random_metadata, random_name, random_passwd, random_email
from model.data_struct.metadata import metadata
from service.entity.user import User


def encryption(orgin_data, method, *args):
    '''
    加密数据
    :param orgin_data:
    :param method:
    :param args:
    :return:
    '''
    pass


def decryption(encry_data, method, *arg):
    '''
    解密数据
    :param encry_data:
    :param method:
    :param arg:
    :return:
    '''
    pass


def authenticate(user_name: str, passwd: str):
    '''
    校验用户名和密码
    :param user_name: 用户名
    :param passwd: 密码
    :return:
    '''
    flag = True
    return flag


def authority(user_name:str,passwd:str,role_name:str):
    '''
    角色授权验证
    :param user_name: 用户名
    :param passwd: 密码
    :param role_name: 角色名
    :return:
    '''
    pass


def insert_user(name, passwd, ip_url, db):
    '''
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(128))
    password = db.Column(db.String(64))
    phone_number = db.Column(db.String(64))
    email = db.Column(db.String(64))
    token = db.Column(db.String(256))
    ip_url = db.Column(db.String(256))
    role_code = db.Column(db.String(64))
    '''
    u = User.query.order_by(name='id').first()
    user = User(id=str(int(u.id) + 1), name=name, password=passwd, ip_url=ip_url)
    db.session.add(user)
    db.seesion.commit()


def insert_random_user():
    '''

    :return:
    '''
    name = metadata().set('name', 1, random_name(100))
    passwd = metadata().set('password', 1, random_passwd(100, 8))
    email = metadata().set('email', 1, random_email(100, ['a', 'b', 'c', 'd', 'e', 'f']))
    phone = metadata().set('phone_number', 0, [1889000, 18891000])
    datas = [name, passwd, email, phone]
    result = random_metadata(100, datas)
    return result
