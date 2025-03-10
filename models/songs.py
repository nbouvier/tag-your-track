from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from ytmusicapi import YTMusic

class Songs:
    def __init__(self, playlist_id):
        self.songs = self.fetch(playlist_id)

    def fetch(self, playlist_id):
        ytmusic = YTMusic("./browser.json")
        playlist = ytmusic.get_playlist(playlist_id)
        return playlist['tracks']

    def build(self):
        layout = MDBoxLayout(orientation='vertical', size_hint_y=None, padding=10, spacing=10)
        layout.bind(minimum_height=layout.setter('height'))

        for song in self.songs:
            song_label = MDLabel(text=song['title'], size_hint_y=None, height=40)
            layout.add_widget(song_label)

        return layout
