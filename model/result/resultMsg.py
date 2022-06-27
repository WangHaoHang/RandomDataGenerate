class resultMsg(object):
    '''
    统一返回消息结构体
    '''
    def __init__(self):
        '''

        '''
        self.code = '0'
        self.msg = 'success'
        self.data = None

    def error(self):
        '''

        :return:
        '''
        self.code = '-1'
        self.msg = 'failed'
        return self

    # def __repr__(self):
    #     return repr((self.code,self.msg,self.data))
