from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def build(self):
        title_label = MDLabel(text=self.title, size_hint_y=None, height=20)
        artist_label = MDLabel(text=self.artist, size_hint_y=None, height=20)

        layout = MDBoxLayout(orientation='vertical', size_hint_y=None, height=40, padding=5)
        layout.add_widget(title_label)
        layout.add_widget(artist_label)

        card = MDCard(size_hint_y=None, height=50)
        card.add_widget(layout)

        return card