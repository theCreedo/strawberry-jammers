from jam.app import DB
from flask_user import UserMixin
from jam.users.helpers import hash_pwd


class User(DB.Model, UserMixin):
    __tablename__ = 'users'

    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(255))
    email = DB.Column(DB.String(255))
    fname = DB.Column(DB.String(255))
    lname = DB.Column(DB.String(255))
    password = DB.Column(DB.String(255))
    is_auth = DB.Column(DB.Integer)
    is_fitted = DB.Column(DB.Integer)

    def __init__(self, dictionary):
        self.is_auth = dictionary['is_auth']
        self.is_fitted = dictionary['is_fitted']
        self.username = dictionary['username']
        self.email = dictionary['email']
        self.fname = dictionary['fname']
        self.lname = dictionary['lname']
        self.password = hash_pwd(dictionary['password'])

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)
