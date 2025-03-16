from kivymd.uix.list import ThreeLineAvatarIconListItem

class SongCard(ThreeLineAvatarIconListItem):
    def __init__(self, title, artist, thumbnail, **kwargs):
        self.title = title
        self.artist = artist
        self.thumbnail = thumbnail
        super().__init__(**kwargs)