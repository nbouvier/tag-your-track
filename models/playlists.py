from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
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
