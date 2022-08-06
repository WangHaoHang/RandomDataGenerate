from service.redis_util import singleton

path_url = 'C:/Users/Hang/PycharmProjects/RandomDataGenerate/model/datas/translate/'


@singleton
class TranslateService(object):
    def __init__(self):
        pass

    def get_translate_file(self, filename: str, pageindex: int, pagesize: int):
        lines = []
        with open(path_url + filename + '.txt', 'r', encoding='utf-8') as fd:
            lines = fd.readlines()
            fd.close()
        datas = self.__filter_lines(lines)
        return datas

    def compute_sentense(self, datas: []):
        sentenses_count = []
        sentenses = []
        size = len(datas)
        for i in range(size // 2):
            count = 0
            chap_index = 2 * i
            content_index = 2 * i + 1
            sentenses.append(datas[chap_index])
            count += 1
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

    def save_translate_file(self, filename: str, origin_data, translate_data, pagesize):
        pass


if __name__ == '__main__':
    trans_utils = TranslateService()
    datas = trans_utils.get_translate_file('Timid Lucy', 1, 10)
    print(len(datas))
    sen_count, sens = trans_utils.compute_sentense(datas)
    print(sen_count)
    print(sens)
