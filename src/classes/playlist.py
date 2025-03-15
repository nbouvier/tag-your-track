from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage import FitImage
from kivymd.uix.card import MDCard

class Playlist:
    def __init__(self, playlist_id, title, thumbnail_url, on_release_callback):
        self.playlist_id = playlist_id
        self.title = title
        self.thumbnail_url = thumbnail_url
        self.on_release_callback = on_release_callback

    def build(self):
        label = MDLabel(text=self.title, size_hint_y=None, height=40)
        thumbnail = FitImage(source=self.thumbnail_url, size_hint_x=None, width=40)

        layout = MDBoxLayout(orientation='horizontal', size_hint_y=None, height=40, padding=5)
        layout.add_widget(thumbnail)
        layout.add_widget(label)

        card = MDCard(size_hint_y=None, height=50, on_release=lambda x: self.on_release_callback(self.playlist_id))
        card.add_widget(layout)

        return card
