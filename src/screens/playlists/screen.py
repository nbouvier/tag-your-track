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
            playlist_card = PlaylistCard(
                playlist['playlistId'],
                playlist['title'],
                playlist['thumbnails'][0]['url'],
                self.load_songs
            )
            self.ids.playlists_container.add_widget(playlist_card)

    def load_songs(self, playlist_id):
        self.ids.songs_container.clear_widgets()

        songs = self.app.ytmusic.get_playlist(playlist_id)['tracks']
        for song in songs:
            song_card = PlaylistSongCard(
                title=song['title'],
                artist=song.get('artists', [{'name': 'Unknown'}])[0]['name']
            )
            self.ids.songs_container.add_widget(song_card)
