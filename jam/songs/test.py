from genius import *
from settings import *

sets = [['What a beautiful name', '10,000 reasons bless the Lord', 'He is exalted'], ['Touch the sky', 'Oceans']]

g = Genius(GENIUS_KEY)

for s in sets:
	sset = SongSet({'name': 'im a songset', 'key': '242iuh', 'songs': []})

	for song in s:
		searchresults = g.search(song)
		# send searchresults to frontend
		# get song entry back
		songentry = g.hitstoreadable(searchresults)[0]
		lyrics = g.get_lyrics(songentry['api_path'])
		songentry['lyrics'] = lyrics
		newsong = Song(songentry)
		sset.songs.append(newsong)
		with jam_app.app_context():
			DB.session.add(sset)
			DB.session.commit()
			