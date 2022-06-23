from service.model import Model, StringField


class User(Model):
    id = StringField(name='id', primary_key=True)
    name = StringField(name='name')
    password = StringField(name='passwd')
    phone_number = StringField(name='phone_number')
    email = StringField(name='email')
    token = StringField(name='token')
    ip_url = StringField(name='ip_url')
    role_code = StringField(name='role_code')

    def __init__(self):
        super(User, self).__init__()


if __name__ == '__main__':
    user = User()
    # user.create()
    user.id = '1'
    user.name = 'hang'
    user.email = "hang@qq.com"
    user.password = "123"
    user.phone_number = "18963607215"
    user.ip_url = "http:localhost"
    user.role_code = "admin"
    user.token = "123"
    print(user.insert())
