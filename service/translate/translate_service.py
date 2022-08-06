from service.redis_util import singleton

path_url = 'C:/Users/Hang/PycharmProjects/RandomDataGenerate/model/datas/translate/'


@singleton
class TranslateService(object):
    def __init__(self):
        pass

    def get_translate_file(self, filename: str, pagesize: int):
        lines = []
        with open(path_url + filename, 'r', encoding='utf-8') as fd:
            lines = fd.readlines()
            fd.close()
        datas = self.__filter_lines(lines)
        return datas

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
    datas = trans_utils.get_translate_file('Timid Lucy.txt', 10)
    print(len(datas))
