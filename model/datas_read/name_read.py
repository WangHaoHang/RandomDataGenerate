import json

import numpy as np
import os
import pandas as pd
import json as js
import datetime

DATA_DIR = os.path.dirname(os.path.abspath('__file__'))
print(DATA_DIR)
# DATA_URL = os.path.dirname(DATA_DIR)+'/datas'
DATA_URL = os.path.join(DATA_DIR, 'model/datas')
print(DATA_URL)


def read_english_chinese_dictionary():
    '''

    :return:
    '''
    dictionary = {}
    filename = 'english_chinese_dictionary.txt'
    fd = open(DATA_URL + '/chinese_name/' + filename, 'r', encoding='utf-8')
    lines = fd.readlines()
    for line in lines:
        datas = line.split('   ')
        if len(datas) == 2:
            tmp = datas[1].strip().split('.')
            dictionary[datas[0]] = tmp
        else:
            dictionary[datas[0]] = []
    return dictionary


def read_first_name(filename):
    '''

    :param filename:
    :return:
    '''
    first_name = []
    fd = open(DATA_URL + '/chinese_name/' + filename, 'r', encoding='utf-8')
    lines = fd.readlines()
    line = lines[0]
    segs = line.split(',')
    flag = True
    for seg in segs:
        if seg.startswith("万俟"):
            flag = False
        if not flag:
            first_name.append(seg[0:2])
            first_name.append(seg[2:])
        else:
            for x in seg:
                first_name.append(x)
    return first_name


def read_last_name(filename):
    '''

    :param filename:
    :return:
    '''
    last_name = set()
    fd = open(DATA_URL + '/chinese_name/' + filename, 'r', encoding='utf-8')
    line = fd.readline()
    segs = line.split(',')
    for seg in segs:
        seg_len = len(seg) - 1
        for i in range(seg_len):
            last_name.add(seg[i])
            last_name.add(seg[i:i + 2])
        last_name.add(seg[seg_len])
    return list(last_name)


if __name__ == '__main__':
    # print(DATA_URL)
    # data = random_stu(100, ['语文', '数学', '英语', '化学', '物理', '生物'])
    # print(data)
    # data = np.random.randint(10, 100, 3).astype(str)
    # print(data)
    dicti = read_english_chinese_dictionary()
    for k in dicti.keys():
        print(k.upper())
    print(len(dicti.keys()))
