from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from ytmusicapi import YTMusic

from src.screens.home.screen import Home
from src.screens.playlists.screen import Playlists
from src.screens.tags.screen import Tags
from src.database import init_database

PLAYLIST_NAME = "TagYourTracks"
PLAYLIST_DESCRIPTION = "Your tagged tracks playlist"

class TagYourTracks(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Tag Your Tracks"
        
        self.db = init_database()
        self.ytmusic = YTMusic("./browser.json")
        
        self.playlist_id = self.init_playlist_id()

    def init_playlist_id(self):
        playlists = self.ytmusic.get_library_playlists()
        playlist = next(iter([p for p in playlists if p['title'] == PLAYLIST_NAME]), None)
        
        return playlist['playlistId'] if playlist else self.ytmusic.create_playlist(PLAYLIST_NAME, PLAYLIST_DESCRIPTION)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        
        # Load KV file
        root = Builder.load_file('src/main.kv')
        
        # Initialize screens
        screen_manager = root.ids.screen_manager
        screen_manager.add_widget(Home(app=self, name='home'))
        screen_manager.add_widget(Playlists(app=self, name='playlists'))
        screen_manager.add_widget(Tags(app=self, name='tags'))
        
        return root

    def switch_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name
