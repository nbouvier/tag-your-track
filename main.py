from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from models.playlists import Playlists
from models.songs import Songs
from models.tag_management import TagManagement
from ytmusicapi import YTMusic

class TagYourTracks(MDApp):
    def build(self):
        self.ytmusic = YTMusic("./browser.json")

        self.main_layout = MDBoxLayout(orientation='horizontal')

        playlist_layout = Playlists(self.ytmusic, self.on_playlist_click).build()
        scroll_view_playlists = MDScrollView()
        scroll_view_playlists.add_widget(playlist_layout)

        self.playlist_container = MDBoxLayout(orientation='vertical')
        self.playlist_container.add_widget(scroll_view_playlists)

        self.tag_management_container = MDBoxLayout(orientation='vertical')
        self.tag_management = TagManagement()
        tag_management_layout = self.tag_management.build()
        self.tag_management_container.add_widget(tag_management_layout)

        self.songs_container = MDBoxLayout(orientation='vertical')

        right_container = MDBoxLayout(orientation='vertical')
        right_container.add_widget(self.tag_management_container)
        right_container.add_widget(self.songs_container)

        self.main_layout.add_widget(self.playlist_container)
        self.main_layout.add_widget(right_container)

        return self.main_layout

    def on_playlist_click(self, playlist_id):
        self.songs_container.clear_widgets()
        songs_layout = Songs(self.ytmusic, playlist_id).build()
        scroll_view_songs = MDScrollView()
        scroll_view_songs.add_widget(songs_layout)
        self.songs_container.add_widget(scroll_view_songs)

if __name__ == '__main__':
    TagYourTracks().run()
