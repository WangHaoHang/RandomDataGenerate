class resultMsg(object):

    def __init__(self):
        self.code = '0'
        self.msg = 'success'
        self.data = None

    def error(self):
        self.code = '-1'
        self.msg = 'failed'
        return self

    # def __repr__(self):
    #     return repr((self.code,self.msg,self.data))
