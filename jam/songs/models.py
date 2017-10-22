from jam.app import DB
#from flask_user import UserMixin
from jam.users.helpers import hash_pwd

songs_join = DB.Table('songs_join',
	DB.Column('song_id', DB.Integer, DB.ForeignKey('songs.id'), primary_key=True),
	DB.Column('songset_id', DB.Integer, DB.ForeignKey('songsets.id'), primary_key=True))



class Song(DB.Model):
    __tablename__ = 'songs'

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(255))
    genius_id = DB.Column(DB.Integer)
    lyrics = DB.Column(DB.Text)

    def __init__(self, dictionary):
        self.name = dictionary['name']








class SongSet(DB.Model):
	__tablename__ = 'songsets'

	id = DB.Column(DB.Integer, primary_key=True)
	name = DB.Column(DB.String(255)) #name of group/set
	key = DB.Column(DB.String(6)) #url key
	songs_join = DB.relationship('Song', secondary=songs_join, backref=DB.backref('songs', lazy=True))

	def __init__(self, dictionary):
		self.name = dictionary['name']
		self.key = dictionary['key']
		self.songs = dictionary['songs']