import logging

from service.model import Model, StringField


class User(Model):
    id = StringField(name='id', primary_key=True)
    name = StringField(name='name',unique_key=True,is_null=False)
    password = StringField(name='passwd',is_null=False)
    phone_number = StringField(name='phone_number')
    email = StringField(name='email')
    token = StringField(name='token')
    ip_url = StringField(name='ip_url')
    role_code = StringField(name='role_code')

    def __init__(self):
        super(User, self).__init__()

    def get_next_id(self):
        sql_statement = 'select max(id) from user'
        id_num = None
        try:
            cur = self.conn.cursor()
            cur.execute(sql_statement)
            self.conn.commit()
            id_num = cur.fetchone()[0]
            cur.close()
        except Exception as e:
            logging.error(e)
        if id_num is None:
            id_num = 0
        else:
            id_num = int(id_num) + 1
        return str(id_num)

if __name__ == '__main__':
    user = User()
    user.id = user.get_next_id()
    print(user.id)
    # user.create()
    # user.id = '1'
    user.name = 'hang1'
    user.email = "hang@qq.com"
    user.password = "123"
    # user.phone_number = "18963607215"
    # user.ip_url = "http:localhost"
    # user.role_code = "admin"
    # user.token = "123"
    print(user.insert())
