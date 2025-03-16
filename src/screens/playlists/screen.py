from kivymd.uix.screen import MDScreen
from src.classes.track import Track
from .playlist_card.component import PlaylistCard
from .playlist_track_card.component import PlaylistTrackCard

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
            playlist_card = PlaylistCard(playlist, self.load_tracks)
            self.ids.playlists_container.add_widget(playlist_card)

    def load_tracks(self, playlist):
        self.ids.tracks_container.clear_widgets()
        for track in playlist.get_tracks():
            track_card = PlaylistTrackCard(track)
            self.ids.tracks_container.add_widget(track_card)
