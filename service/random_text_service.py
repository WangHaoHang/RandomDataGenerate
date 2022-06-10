from model.datas_read.name_read import read_first_name, read_last_name
import datetime
import numpy as np
import json
from model.data_struct.metadata import metadata


def random_text(text: [], num: int) -> []:
    '''
    从text中随机选择num个数据
    :param text: 源数据
    :param num: 个数
    :return:
    '''
    size = len(text)
    result = []
    for i in range(num):
        result.append(text[np.random.randint(0, size)])
    return result


def random_name(num: int):
    ''' this is a function to radom num names
    :param num: the number of the sample data
    :return:
    '''
    first_name = read_first_name('百家姓.txt')
    last_name = read_last_name('滕王阁序.txt')
    x_name = random_text(first_name, num)
    y_name = random_text(last_name, num)
    z_name = []
    for i in range(len(x_name)):
        z = x_name[i] + y_name[i]
        z_name.append(z)
    return z_name


def random_stu(num: int, subjects: []):
    '''
    学生成绩固定阈值设置
    :param num:
    :param subjects:
    :return:
    '''
    stu_info = {}
    z_name = random_name(num)
    sex = random_text([0, 1], num)
    id_start = int(datetime.datetime.now().strftime('%Y%m%d%H'))
    stu_info['ID'] = list([x for x in range(id_start, id_start + num)])
    stu_info['姓名'] = list(z_name)
    stu_info['性别'] = list(sex)
    for subject in subjects:
        stu_info[subject] = list(np.random.randint(60, 150, num).astype(float))
    return json.dumps(stu_info, ensure_ascii=False)


def random_stu_score_threshold_type(num: int, subjects: []):
    '''
    学生成绩可修改阈值设置
    :param num:
    :param subjects:
    subject :
    {
        id: i,
        subject: 'math',
        max: 100,
        min: 0,
        type: 0
    }
    x = random_stu_threshold(100,[{id:0,subject:'math',max:100,min:0,type:0}])
    :return:
    '''
    stu_info = {}
    z_name = random_name(num)
    sex = random_text([0, 1], num)
    id_start = int(datetime.datetime.now().strftime('%Y%m%d%H'))
    stu_info['ID'] = list([x for x in range(id_start, id_start + num)])
    stu_info['姓名'] = list(z_name)
    stu_info['性别'] = list(sex)
    for item in subjects:
        stu_info[item['subject']] = list(np.random.randint(item['min'], item['max'], num).astype(float))
    return json.dumps(stu_info, ensure_ascii=False)


def random_stu_score_threshold(num: int, subjects: dict):
    '''
    学生成绩可修改阈值设置
    :param num:
    :param subjects:
    x = random_stu_threshold(100,{'math':[100,150],'english':[80,100]}
    :return:
    '''
    stu_info = {}
    z_name = random_name(num)
    sex = random_text([0, 1], num)
    id_start = int(datetime.datetime.now().strftime('%Y%m%d%H'))
    stu_info['ID'] = list([x for x in range(id_start, id_start + num)])
    stu_info['姓名'] = list(z_name)
    stu_info['性别'] = list(sex)
    for k, v in subjects.items():
        stu_info[k] = list(np.random.randint(v[0], v[-1], num).astype(float))
    return json.dumps(stu_info, ensure_ascii=False)


def random_metadata(num: int, datas: []):
    '''
    随机根据元数据进行数据生成功能
    :param num:
    :param datas:
    :return:
    '''
    result = {}
    id_start = int(datetime.datetime.now().strftime('%Y%m%d%H'))
    result['id'] = list([x for x in range(id_start, id_start + num)])
    for data in datas:
        if data.type == 0:
            result[data.name] = list(np.random.randint(data.data[0], data.data[-1], num).astype(float))
        elif data.type == 1:
            result[data.name] = random_text(data.data, num)
        else:
            pass
    return result


def random_passwd(num: int, passwd_num: int):
    '''
    随机生成密码
    :param num:
    :param passwd_num:
    :return:
    '''
    meta_data = 'abcdefghijklmnopqrstuvwxyz.,!@#$%^&*()[]+|?ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    for i in range(num):
        tmp = random_text(meta_data, passwd_num)
        r = ''
        for t in tmp:
            r += t
        result.append(r)
    return result


def random_email(num: int, prefix: []):
    '''
    随机生成email
    :param num: 个数
    :param prefix: 前缀
    :return: result : 结果
    examples:
        result = random_email(100,['a','b','c','d'])
    '''
    suffix = ['@qq.com', '@163.com', '@126.com', '@foxmail.com', '@139.com', '@189.com']
    result = []
    prefix_result = random_text(prefix, num)
    suffix_result = random_text(suffix, num)
    for i in range(num):
        result.append(prefix_result[i] + suffix_result[i])
    return result
