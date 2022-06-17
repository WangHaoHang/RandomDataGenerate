import pandas as pd


def save_csv(path: str, data: {}):
    '''
    保存数据到CSV文件中
    :param path: 保存路径
    :param data: 保存数据
    :return: flag: True-保存成功  False-保存失败
    '''
    flag = True
    file = pd.DataFrame(data=data)
    try:
        file.to_csv(path_or_buf=path)
    except Exception as e:
        flag = False
        print(e)
    return flag


def save_excel(path: str, data: {}):
    '''
    保存数据到Excel文件中
    :param path: 保存路径
    :param data: 保存数据
    :return: flag: True-保存成功  False-保存失败
    '''
    flag = True
    file = pd.DataFrame(data=data)
    try:
        file.to_excel(path_or_buf=path)
    except Exception as e:
        flag = False
        print(e)
    return flag
