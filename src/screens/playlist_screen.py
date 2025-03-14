from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
from src.components.playlists import Playlists
from src.components.songs import Songs

class PlaylistScreen(MDScreen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.name = 'playlist'
        self.build_layout()
        
    def build_layout(self):
        self.main_layout = MDBoxLayout(orientation='horizontal')

        playlist_layout = Playlists(self.app.ytmusic, self.on_playlist_click).build()
        scroll_view_playlists = MDScrollView()
        scroll_view_playlists.add_widget(playlist_layout)

        self.playlist_container = MDBoxLayout(orientation='vertical')
        self.playlist_container.add_widget(scroll_view_playlists)

        self.songs_container = MDBoxLayout(orientation='vertical')

        self.main_layout.add_widget(self.playlist_container)
        self.main_layout.add_widget(self.songs_container)

        self.add_widget(self.main_layout)

    def on_playlist_click(self, playlist_id):
        self.songs_container.clear_widgets()
        songs_layout = Songs(self.app.ytmusic, playlist_id).build()
        scroll_view_songs = MDScrollView()
        scroll_view_songs.add_widget(songs_layout)
        self.songs_container.add_widget(scroll_view_songs)