import kivy
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.fitimage import FitImage
from kivymd.uix.card import MDCard
from ytmusicapi import YTMusic

class Playlists:
    def __init__(self):
        self.playlists = self.fetch()

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
                thumbnail_url=playlist_data['thumbnails'][0]['url']
            )
            item_layout = playlist.build(self.print_playlist_id)
            layout.add_widget(item_layout)

        return layout

    def print_playlist_id(self, playlist_id):
        print(f"Playlist ID: {playlist_id}")

class Playlist:
    def __init__(self, playlist_id, title, thumbnail_url):
        self.playlist_id = playlist_id
        self.title = title
        self.thumbnail_url = thumbnail_url

    def build(self, on_release_callback):
        playlist_label = MDLabel(text=self.title, size_hint_y=None, height=40)
        thumbnail = FitImage(source=self.thumbnail_url, size_hint_x=None, width=40)

        item_layout = MDBoxLayout(orientation='horizontal', size_hint_y=None, height=40, padding=5)
        item_layout.add_widget(thumbnail)
        item_layout.add_widget(playlist_label)

        card = MDCard(size_hint_y=None, height=50, on_release=lambda x: on_release_callback(self.playlist_id))
        card.add_widget(item_layout)

        return card

class TagYourTracks(MDApp):
    def build(self):
        playlist_layout = Playlists().build()

        scroll_view = MDScrollView()
        scroll_view.add_widget(playlist_layout)

        layout = MDBoxLayout(orientation='vertical')
        layout.add_widget(scroll_view)

        return layout

if __name__ == '__main__':
    TagYourTracks().run()
