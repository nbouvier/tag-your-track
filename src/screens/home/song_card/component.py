from kivymd.uix.card import MDCard

class SongCard(MDCard):
    def __init__(self, title, artist, **kwargs):
        self.title = title
        self.artist = artist
        super().__init__(**kwargs)