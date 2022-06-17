import sqlite3
import logging

'''
基于sqlite3的ORM模型架构
'''


class Field(object):
    '''

    '''

    def __init__(self, name, column_type, primary_key=False, unique_key=False, is_null=True):
        '''

        :param name:
        :param column_type:
        :param primary_key:
        :param unique_key:
        :param is_null:
        '''
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.unique_key = unique_key
        self.is_null = is_null

    def __str__(self):
        '''

        :return:
        '''
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class CharField(Field):
    '''

    '''

    def __init__(self, name, size=255, primary_key=False, unique_key=False, is_null=True):
        '''

        :param name:
        :param size:
        :param primary_key:
        :param unique_key:
        :param is_null:
        '''
        super(StringField, self).__init__(name, 'CHAR(' + str(size) + ")", primary_key=primary_key,
                                          unique_key=unique_key, is_null=is_null)


class StringField(Field):
    '''

    '''

    def __init__(self, name, primary_key=False, unique_key=False, is_null=True):
        '''

        :param name:
        :param primary_key:
        :param unique_key:
        :param is_null:
        '''
        super(StringField, self).__init__(name, 'TEXT', primary_key=primary_key, unique_key=unique_key, is_null=is_null)


class IntegerField(Field):
    '''

    '''

    def __init__(self, name, primary_key=False, unique_key=False, is_null=True):
        '''

        :param name:
        :param primary_key:
        :param unique_key:
        :param is_null:
        '''
        super(IntegerField, self).__init__(name, 'INTEGER', primary_key=primary_key, unique_key=unique_key,
                                           is_null=is_null)


class RealField(Field):
    '''

    '''

    def __init__(self, name, primary_key=False, unique_key=False, is_null=True):
        '''

        :param name:
        :param primary_key:
        :param unique_key:
        :param is_null:
        '''
        super(RealField, self).__init__(name, 'REAL', primary_key=primary_key, unique_key=unique_key, is_null=is_null)


class BlobField(Field):
    '''

    '''

    def __init__(self, name, primary_key=False, unique_key=False, is_null=True):
        '''

        :param name:
        :param primary_key:
        :param unique_key:
        :param is_null:
        '''
        super(BlobField, self).__init__(name, 'BOLB', primary_key=primary_key, unique_key=unique_key, is_null=is_null)


class ModelMetaClass(type):
    '''
    Model元基类
    '''

    def __new__(cls, name, bases, attrs):
        '''

        :param name:
        :param bases:
        :param attrs:
        '''
        print('ModelMetaClass __new__ ', cls, name, bases, attrs)
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
        for k, v in mappings.items():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(object, metaclass=ModelMetaClass):
    '''

    '''

    def __init__(self, **kw):
        '''

        :param kw:
        '''
        super(Model, self).__init__(**kw)
        self.conn = sqlite3.connect("C:/Users/Hang/PycharmProjects/RandomDataGenerate/data.db")

    def __getattr__(self, item):
        '''

        :param item:
        :return:
        '''
        try:
            return self.__dict__[item]
        except KeyError:
            raise AttributeError(r"Model'object has no attribute '%s" % item)

    def __setattr__(self, key, value):
        '''

        :param key:
        :param value:
        :return:
        '''
        self.__dict__[key] = value

    def create(self):
        '''
        创建表
        :return:
        '''
        conditions = []
        for k, v in self.__mappings__.items():
            condition = str(v.name) + ' ' + str(v.column_type)

            '''
                primary_key True 为主键
                unique_key True 为唯一键
                is_null True 可为空
            '''
            if v.primary_key:
                condition += ' PRIMARY KEY'
            if not v.is_null:
                condition += ' NOT NULL'
            if v.unique_key:
                condition += ' UNIQUE'
            conditions.append(condition)
        sql = 'create table %s(%s)' % (self.__table__, ','.join(conditions))
        logging.warning(sql)
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
            cur.close()
        except Exception as e:
            logging.error("create table happens error,the statement of sql :%s,error:%s", sql, e)

    def save(self, **kwargs):
        '''
        保存数据
        :param kwargs: 条件语句
        :return:
        '''
        update_str = []
        condition_str = []

        for k, v in self.__mappings__.items():
            if list(kwargs.keys()).count(k) >= 0:
                v_condition = kwargs.get(k)
                if type(v_condition) == int or type(v_condition) == float:
                    condition_str.append(str(v.name) + '=' + str(v_condition))
                elif type(v_condition) == str:
                    condition_str.append(str(v.name) + '=' + '\'' + str(v_condition) + '\'')
            v_new = getattr(self, k, None)
            if v_new is None:
                continue
            if type(v_new) == int or type(v_new) == float:
                update_str.append(str(v.name) + '=' + str(v_new))
            elif type(v) == str:
                update_str.append(str(v.name) + '=' + '\'' + str(v_new) + '\'')

        sql = 'update %s set %s where %s' % (self.__table__, ' , '.join(update_str), ' and '.join(condition_str))
        logging.warning(sql)
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
            cur.close()
        except Exception as e:
            logging.error("save infomation happens error,the statement of sql :%s,error:%s", sql, e)

    def insert(self):
        '''
        插入数据
        :return:
        '''
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            if v.column_type == 'text':
                args.append('\'' + getattr(self, k, None) + '\'')
            else:
                args.append(str(getattr(self, k, None)))
        sql = 'insert into %s(%s) values(%s)' % (self.__table__, ','.join(fields), ','.join(args))
        logging.warning(sql)
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
            cur.close()
        except Exception as e:
            logging.error("insert data happens error,the statement of sql :%s,error:%s", sql, e)

    def delete(self):
        '''
        删除数据
        :return:
        '''
        update_str = []

        for k, v in self.__mappings__.items():
            v_new = getattr(self, k, None)
            if v_new is None:
                continue
            if type(v_new) == int or type(v_new) == float:
                update_str.append(str(v.name) + '=' + str(v_new))
            elif type(v) == str:
                update_str.append(str(v.name) + '=' + '\'' + str(v_new) + '\'')

        sql = 'delete from %s where %s' % (self.__table__, ' and '.join(update_str))

        logging.warning(sql)
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
            cur.close()
        except Exception as e:
            logging.error("delete data happens error,the statement of sql :%s,error:%s", sql, e)


class User_Test(Model):
    '''

    '''
    id = IntegerField(name='id')
    name = StringField(name='name')
    age = IntegerField(name='age')

    def __init__(self):
        super(User_Test, self).__init__()


if __name__ == '__main__':
    # print(dir(Field))
    user_test = User_Test()
    # 建表语句测试
    # user_test.create()
    # 插入语句测试
    # user_test.id = 2
    # user_test.name = 'hang1'
    # user_test.age = 18
    # user_test.insert()
    # 保存语句测试
    # user_test.id = 1
    # user_test.name = 'hang1'
    # user_test.age = 19
    # user_test.save(name='hang')

    # 删除语句
    user_test.id = 1
    user_test.name = 'hang'
    user_test.age = 19
    user_test.delete()
