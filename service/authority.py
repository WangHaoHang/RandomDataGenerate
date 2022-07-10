from werkzeug.security import generate_password_hash, check_password_hash
from service.random_text_service import random_metadata, random_name, random_passwd, random_email
from model.data_struct.metadata import metadata
from service.entity.user import User

import logging

def encryption(orgin_data, method, *args):
    '''
    加密数据
    :param orgin_data:
    :param method:
    :param args:
    :return:
    '''
    return generate_password_hash(str(orgin_data), method=method)


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
    user = User()
    result = user.query(name=str(user_name))
    if result is None or len(result) == 0:
        return False
    try:
        flag = check_password_hash(result[0][2], passwd)
    except Exception as e:
        logging.error(e)
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


def insert_user(name, passwd, ip_url):
    '''
    插入数据
    :param name: 姓名
    :param passwd: 密码
    :param ip_url:
    :return:
    '''
    user = User()
    user.id = user.get_next_id()
    user.name = name
    user.password = encryption(passwd)
    user.ip_url = ip_url
    return user.insert()

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
