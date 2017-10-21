import requests
from bs4 import BeautifulSoup

# GENIUS_KEY = 'aXVdNmQrmI4YZnwC0swJCq9MubVwMXwhH60qlMO8nBU6XuFMkO-cwc0f3GxG5yWm'
GENIUS_BASE_URL = "http://api.genius.com"

class Genius:
    def __init__(self, genius_key):
        self.genius_key = genius_key
        self.genius_header = {'Authorization': 'Bearer %s' %(genius_key)}

    def get_first_lyrics(self, search_term):
        hits = self.search(song_title)
        readable = self.hitstoreadable(hits)
        if len(readable) > 0:
            song_api_path = readable[0]['api_path']
            return self.get_lyrics(song_api_path)
        return:
            'Could not find lyrics\n'

    def get_lyrics(self, api_path):
        song_url = GENIUS_BASE_URL + api_path
        response = requests.get(song_url, headers=self.genius_header)
        json = response.json()
        path = json['response']['song']['path']
        page_url = 'http://genius.com' + path

        page = requests.get(page_url)
        soup = BeautifulSoup(page.text, 'html.parser')
        div = soup.find('div',{'class': 'song_body-lyrics'})
        lyrics = div.find('p').getText()


    def search(self, search_term):
        search_url = GENIUS_BASE_URL + "/search"
        data = {'q': search_term}

        response = requests.get(search_url, params=data, headers=self.genius_header)
        json = response.json()

        try:
            hits = json["response"]["hits"]
        except KeyError:
            return None

        return hits

    def hitstoreadable(hits):
        return [{'name': hit['result']['title'], 'artist': hit['result']['primary_artist']['name'], 'api_path': hit['result']['api_path']} for hit in hits]

    def get_song_info(id, text_format='dom'):
        song_url = GENIUS_BASE_URL + "/songs" + "/" + str(id)
        data = {'text_format': text_format }

        response = requests.get(song_url, params=data, headers=self.genius_header)
        json = response.json()

        return json





