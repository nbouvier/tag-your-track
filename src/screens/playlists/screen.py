from kivymd.uix.screen import MDScreen
from src.classes.song import Song
from .playlist_card.component import PlaylistCard
from .playlist_song_card.component import PlaylistSongCard

class PlaylistsScreen(MDScreen):
    def __init__(self, app, **kwargs):
        self.app = app
        super().__init__(**kwargs)
        
    def on_kv_post(self, base_widget):
        """Called after kv file is loaded"""
        self.load_playlists()

    def load_playlists(self):
        self.ids.playlists_container.clear_widgets()
        for playlist in self.app.playlists:
            playlist_card = PlaylistCard(playlist, self.load_songs)
            self.ids.playlists_container.add_widget(playlist_card)

    def load_songs(self, playlist):
        self.ids.songs_container.clear_widgets()
        for song in playlist.get_tracks():
            song_card = PlaylistSongCard(song)
            self.ids.songs_container.add_widget(song_card)
