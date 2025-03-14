from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard

class Songs:
    def __init__(self, ytmusic, playlist_id):
        self.ytmusic = ytmusic
        self.playlist_id = playlist_id
        self.songs = []

        self.fetch()

    def fetch(self):
        self.songs = self.ytmusic.get_playlist(self.playlist_id)['tracks']

    def build(self):
        layout = MDBoxLayout(orientation='vertical', size_hint_y=None, padding=10, spacing=10)
        layout.bind(minimum_height=layout.setter('height'))

        for song in self.songs:
            song_layout = Song(
                title=song['title'],
                artist=song.get('artists', [{'name': 'Unknown'}])[0]['name']
            ).build()
            layout.add_widget(song_layout)

        return layout

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def build(self):
        title_label = MDLabel(text=self.title, size_hint_y=None, height=20)
        artist_label = MDLabel(text=self.artist, size_hint_y=None, height=20)

        layout = MDBoxLayout(orientation='vertical', size_hint_y=None, height=40, padding=5)
        layout.add_widget(title_label)
        layout.add_widget(artist_label)

        card = MDCard(size_hint_y=None, height=50)
        card.add_widget(layout)

        return card