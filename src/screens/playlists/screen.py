from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
from src.classes.playlist import Playlist
from src.classes.song import Song

class Playlists(MDScreen):
    def __init__(self, app, **kwargs):
        self.app = app
        super().__init__(**kwargs)
        
    def on_kv_post(self, base_widget):
        """Called after kv file is loaded"""
        self.load_playlists()

    def load_playlists(self):
        self.ids.playlists_container.clear_widgets()

        for playlist in self.app.playlists:
            playlist_layout = Playlist(
                playlist_id=playlist['playlistId'],
                title=playlist['title'],
                thumbnail_url=playlist['thumbnails'][0]['url'],
                on_release_callback=self.load_songs
            ).build()
            self.ids.playlists_container.add_widget(playlist_layout)

    def load_songs(self, playlist_id):
        self.ids.songs_container.clear_widgets()

        songs = self.app.ytmusic.get_playlist(playlist_id)['tracks']
        for song in songs:
            song_layout = Song(
                title=song['title'],
                artist=song.get('artists', [{'name': 'Unknown'}])[0]['name']
            ).build()
            self.ids.songs_container.add_widget(song_layout)
