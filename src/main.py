from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from src.database import Session, init_database
from src.screens.playlist_screen import PlaylistScreen
from src.screens.tag_list_screen import TagListScreen
from src.screens.home_screen import HomeScreen
from ytmusicapi import YTMusic

class TagYourTracks(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        init_database()
        self.db = Session()
        self.ytmusic = YTMusic("./browser.json")
        self.playlist_id = None
        self.screen_manager = MDScreenManager()
        self.bottom_navigation = MDBottomNavigation()
        self.init_playlist_id()

    def init_playlist_id(self):
        playlists = self.ytmusic.get_library_playlists()
        playlist = next((p for p in playlists if p['title'] == 'TagYourTrack'), None)
        
        if not playlist:
            self.playlist_id = self.ytmusic.create_playlist('TagYourTrack', 'Playlist for tagged songs')
        else:
            self.playlist_id = playlist['playlistId']

    def build(self):
        # Create bottom navigation items
        home_item = MDBottomNavigationItem(name='home', text='Home', icon='home')
        home_item.add_widget(HomeScreen(self))

        playlist_item = MDBottomNavigationItem(name='playlists', text='Playlists', icon='playlist-music')
        playlist_item.add_widget(PlaylistScreen(self))

        tags_item = MDBottomNavigationItem(name='tags', text='Tags', icon='tag')
        tags_item.add_widget(TagListScreen(self))

        # Add items to bottom navigation
        self.bottom_navigation.add_widget(home_item)
        self.bottom_navigation.add_widget(playlist_item)
        self.bottom_navigation.add_widget(tags_item)

        return self.bottom_navigation

    def on_stop(self):
        if self.db:
            self.db.close()
            Session.remove()
