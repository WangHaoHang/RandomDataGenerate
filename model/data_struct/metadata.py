class metadata(object):
    def __init__(self):
        self.name= ""
        self.type = 0 # 0: 阈值，1: 枚举
        self.data = []

    def set(self,name,type,data):
        self.name = name
        self.type = type
        self.data = data
        return self