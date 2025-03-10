import kivy
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.fitimage import FitImage
from kivymd.uix.card import MDCard
from ytmusicapi import YTMusic

class Playlists:
    def __init__(self, on_playlist_click):
        self.playlists = self.fetch()
        self.on_playlist_click = on_playlist_click

    def fetch(self):
        ytmusic = YTMusic("./browser.json")
        return ytmusic.get_library_playlists()

    def build(self):
        layout = MDBoxLayout(orientation='vertical', size_hint_y=None, padding=10, spacing=10)
        layout.bind(minimum_height=layout.setter('height'))

        for playlist_data in self.playlists:
            playlist = Playlist(
                playlist_id=playlist_data['playlistId'],
                title=playlist_data['title'],
                thumbnail_url=playlist_data['thumbnails'][0]['url'],
                on_release_callback=self.on_playlist_click
            )
            item_layout = playlist.build()
            layout.add_widget(item_layout)

        return layout

class Playlist:
    def __init__(self, playlist_id, title, thumbnail_url, on_release_callback):
        self.playlist_id = playlist_id
        self.title = title
        self.thumbnail_url = thumbnail_url
        self.on_release_callback = on_release_callback

    def build(self):
        playlist_label = MDLabel(text=self.title, size_hint_y=None, height=40)
        thumbnail = FitImage(source=self.thumbnail_url, size_hint_x=None, width=40)

        item_layout = MDBoxLayout(orientation='horizontal', size_hint_y=None, height=40, padding=5)
        item_layout.add_widget(thumbnail)
        item_layout.add_widget(playlist_label)

        card = MDCard(size_hint_y=None, height=50, on_release=lambda x: self.on_release_callback(self.playlist_id))
        card.add_widget(item_layout)

        return card

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

class TagYourTracks(MDApp):
    def build(self):
        self.main_layout = MDBoxLayout(orientation='horizontal')

        playlist_layout = Playlists(self.on_playlist_click).build()
        scroll_view_playlists = MDScrollView()
        scroll_view_playlists.add_widget(playlist_layout)

        self.playlist_container = MDBoxLayout(orientation='vertical')
        self.playlist_container.add_widget(scroll_view_playlists)

        self.songs_container = MDBoxLayout(orientation='vertical')

        self.main_layout.add_widget(self.playlist_container)
        self.main_layout.add_widget(self.songs_container)

        return self.main_layout

    def on_playlist_click(self, playlist_id):
        self.songs_container.clear_widgets()
        songs_layout = Songs(playlist_id).build()
        scroll_view_songs = MDScrollView()
        scroll_view_songs.add_widget(songs_layout)
        self.songs_container.add_widget(scroll_view_songs)

if __name__ == '__main__':
    TagYourTracks().run()
