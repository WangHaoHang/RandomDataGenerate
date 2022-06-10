from app import db


class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(128))
    password = db.Column(db.String(64))
    phone_number = db.Column(db.String(64))
    email = db.Column(db.String(64))
    token = db.Column(db.String(256))
    ip_url = db.Column(db.String(256))
    role_code = db.Column(db.String(64))

    def __repr__(self):
        return '<Role %r>' % self.name

if __name__ == '__main__':
    db.create_all()
    # admin = User(id='1',name='hang',password='123',phone_number='18963607215',email='hang@qq.com')
    # guest = User(id='2',name='haha',password='123',phone_number='18963607215',email='hang@qq.com')
    # db.session.add(admin)
    # db.session.add(guest)
    # db.session.commit()
    # print(User.query.all())
    # print(User.query.filter_by(id='1').first())
