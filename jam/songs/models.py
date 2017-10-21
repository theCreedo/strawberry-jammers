from jam.app import DB
from flask_user import UserMixin
from jam.users.helpers import hash_pwd


class Song(DB.Model, UserMixin):
    __tablename__ = 'songs'

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(255))

    def __init__(self, dictionary):
        self.name = dictionary['name']