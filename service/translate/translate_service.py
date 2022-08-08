import os
from service.redis_util import singleton
path_url = 'C:/Users/Hang/PycharmProjects/RandomDataGenerate/model/datas/translate/'

'''
数据保存格式
|4 byte|n byte|
|头部|单行数据|
头部: 单行数据长度（包含头部)
单行数据: 原文&译文
'''

@singleton
class TranslateService(object):
    def __init__(self):
        pass

    def get_translate_file(self, filename: str, pageindex: int, pagesize: int):
        title = ''
        result = []
        lines = []
        with open(path_url + filename + '.txt', 'r', encoding='utf-8') as fd:
            lines = fd.readlines()
            fd.close()
        lines = self.__filter_lines(lines)
        sen_count, sentenses = self.compute_sentense(lines)
        print(sen_count)
        pre_total_count = (pageindex - 1) * pagesize
        index = 0
        for index in range(len(sen_count)):
            if pre_total_count > sen_count[index]:
                pre_total_count -= sen_count[index]
            else:
                break
        if pre_total_count >= 0:
            title = sentenses[2 * index]
            if sen_count[index] < pre_total_count + pagesize:
                pagesize = sen_count[index] - pre_total_count
            for i in range(pagesize):
                result.append([sentenses[2 * index + 1][i] + '.', ''])
        return title, result

    def compute_sentense(self, datas: []):
        sentenses_count = []
        sentenses = []
        size = len(datas)
        for i in range(size // 2):
            count = 0
            chap_index = 2 * i
            content_index = 2 * i + 1
            sentenses.append(datas[chap_index])
            sentense = str(datas[content_index]).split(".")
            count += len(sentense)
            sentenses_count.append(count)
            sentenses.append(sentense)
        return sentenses_count, sentenses

    def __filter_lines(self, lines):
        new_lines = []
        new_lines_str = ''
        for line in lines:
            if line.startswith('CHAPTER'):
                if new_lines_str == '':
                    new_lines.append(line.strip())
                else:
                    new_lines.append(new_lines_str)
                    new_lines_str = ''
                    new_lines.append(line.strip())
            tmp = str(line).strip()
            if tmp is not None and tmp != '':
                new_lines_str += tmp
        if new_lines_str != '':
            new_lines.append(new_lines_str)
        return new_lines

    def save_translate_file(self, filename: str, datas: [], pageindex: int, pagesize: int):
        '''

        :param filename:
        :param datas:
        :param pageindex:
        :param pagesize:
        :return:
        '''
        fd = None
        if os.path.exists(path_url + filename + '_translate.txt'):
            fd = open(path_url + filename + '_translate.txt', '+', encoding='utf-8')
        else:
            fd = open(path_url + filename + '_translate.txt', 'x', encoding='utf-8')

    def write_line(self, fd, line: str):
        line_bytes = line.encode('utf-8')
        bytes_count = len(line_bytes) + 4
        fd.write(bytes_count.to_bytes(4, byteorder='big'))
        fd.write(line_bytes)


if __name__ == '__main__':
    # trans_utils = TranslateService()
    # title, result = trans_utils.get_translate_file('Timid Lucy', 1, 20)
    # print(title)
    # print(result)
    a = 'hello world'
    b = a.encode('utf-8')
    t = len(b) + 4
    z = t.to_bytes(4, byteorder='big')
    print(int.from_bytes(z, byteorder='big'))
