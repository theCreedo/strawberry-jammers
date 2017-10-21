from jam.app import DB
#from flask_user import UserMixin
from jam.users.helpers import hash_pwd


class Song(DB.Model):
    __tablename__ = 'songs'

    name = DB.Column(DB.String(255))
    genius_id = DB.Column(DB.Integer, primary_key=True)

    def __init__(self, dictionary):
        self.name = dictionary['name']

class SongSet(DB.Model):
	__tablename__ = 'songsets'

	id = DB.Column(DB.Integer, primary_key=True)
	name = DB.Column(DB.String(255)) #name of group/set
	key = DB.Column(DB.String(6)) #url key
	songs = DB.relationship('Song', lazy=False)

	def __init__(self, dictionary):
		self.name = dictionary['name']