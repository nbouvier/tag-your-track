import kivy
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.fitimage import FitImage
from kivy.uix.widget import Widget
from ytmusicapi import YTMusic

class PlaylistApp(MDApp):
    def build(self):
        playlist_layout = self.build_playlists_layout()

        scroll_view = MDScrollView()
        scroll_view.add_widget(playlist_layout)

        layout = MDBoxLayout(orientation='vertical')
        layout.add_widget(scroll_view)

        return layout

    def build_playlists_layout(self):
        playlist_layout = MDBoxLayout(orientation='vertical', size_hint_y=None, padding=10, spacing=10)
        playlist_layout.bind(minimum_height=playlist_layout.setter('height'))

        for playlist in self.fetch_playlists():
            item_layout = self.build_playlist_item(playlist)
            playlist_layout.add_widget(item_layout)

        return playlist_layout

    def fetch_playlists(self):
        ytmusic = YTMusic("./browser.json")

        return ytmusic.get_library_playlists()

    def build_playlist_item(self, playlist):
        playlist_label = MDLabel(text=playlist['title'], size_hint_y=None, height=40)

        thumbnail_url = playlist['thumbnails'][0]['url']
        thumbnail = FitImage(source=thumbnail_url, size_hint_x=None, width=40)

        item_layout = MDBoxLayout(orientation='horizontal', size_hint_y=None, height=40, padding=5)
        item_layout.add_widget(thumbnail)
        item_layout.add_widget(playlist_label)

        return item_layout

if __name__ == '__main__':
    PlaylistApp().run()
