from kivymd.app import MDApp
from kivy.lang import Builder
from ytmusicapi import YTMusic
from src.database import init_database
from src.classes.playlist import Playlist
from src.screens.home.screen import HomeScreen
from src.screens.playlists.screen import PlaylistsScreen
from src.screens.tags.screen import TagsScreen

PLAYLIST_NAME = "TagYourTracks"
PLAYLIST_DESCRIPTION = "Your tagged tracks playlist"

class TagYourTracks(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Tag Your Tracks"
        
        self.db = init_database()
        self.ytmusic = YTMusic("./browser.json")
        
        self.load_playlists()
        self.init_playlist()

    def load_playlists(self):
        self.playlists = []
        for playlist in self.ytmusic.get_library_playlists():
            if playlist['playlistId'] not in ('LM', 'SE'):
                self.playlists.append(Playlist(playlist, ytmusic=self.ytmusic))

    def init_playlist(self):
        self.playlist = next(iter([p for p in self.playlists if p.get_title() == PLAYLIST_NAME]), None)

        if not self.playlist:
            playlist_id = self.ytmusic.create_playlist(PLAYLIST_NAME, PLAYLIST_DESCRIPTION)
            self.playlist = Playlist(self.ytmusic.get_playlist(playlist_id), loaded=True)
            self.playlists.insert(0, self.playlist)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        
        # Load KV file
        root = Builder.load_file('src/main.kv')
        
        # Initialize screens
        screen_manager = root.ids.screen_manager
        screen_manager.add_widget(HomeScreen(app=self, name='home'))
        screen_manager.add_widget(PlaylistsScreen(app=self, name='playlists'))
        screen_manager.add_widget(TagsScreen(app=self, name='tags'))
        
        return root

    def switch_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name
