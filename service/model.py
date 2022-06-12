import sqlite3


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'text')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'INTEGER')


class RealField(Field):
    def __init__(self, name):
        super(RealField, self).__init__(name, 'REAL')


class BlobField(Field):
    def __init__(self, name):
        super(BlobField, self).__init__(name, 'BOLB')


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
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
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
        self.conn = sqlite3.connect("C:/Users/Hang/PycharmProjects/RandomDataGenerate/data.db")

    def __getattr__(self, item):
        try:
            return self.__dict__[item]
        except KeyError:
            raise AttributeError(r"Model'object has no attribute '%s" % item)

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def create(self):
        condition = []
        for k, v in self.__mappings__.items():
            condition.append(str(v.name) + ' ' + str(v.column_type))
        sql = 'create table %s(%s)' % (self.__table__, ','.join(condition))
        print(sql)
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()

    def save(self, **kwargs):
        update_str = []
        condition_str = []

        for k, v in self.__mappings__.items():
            if kwargs.keys().index(k) >= 0:
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

        sql = 'update table %s set %s where %s' % (self.__table__, 'and'.join(update_str), 'and'.join(condition_str))
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()

    def insert(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            if v.column_type == 'text':
                args.append('\''+getattr(self, k, None)+'\'')
            else:
                args.append(str(getattr(self, k, None)))
        sql = 'insert into %s(%s) values(%s)' % (self.__table__, ','.join(fields), ','.join(args))
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()

    def delete(self):
        update_str = []

        for k, v in self.__mappings__.items():
            v_new = getattr(self, k, None)
            if v_new is None:
                continue
            if type(v_new) == int or type(v_new) == float:
                update_str.append(str(v.name) + '=' + str(v_new))
            elif type(v) == str:
                update_str.append(str(v.name) + '=' + '\'' + str(v_new) + '\'')

        sql = 'delete table %s where %s' % (self.__table__, 'and'.join(update_str))
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()


class User_Test(Model):
    id = IntegerField(name='id')
    name = StringField(name='name')
    age = IntegerField(name='age')

    def __init__(self):
        super(User_Test, self).__init__()


if __name__ == '__main__':
    # print(dir(Field))
    user_test = User_Test()
    user_test.create()
    # user_test.id = 1
    # user_test.name = 'hang'
    # user_test.age = 18
    # user_test.insert()
