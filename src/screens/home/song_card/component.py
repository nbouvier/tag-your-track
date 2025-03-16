from kivymd.uix.list import ThreeLineAvatarIconListItem

class SongCard(ThreeLineAvatarIconListItem):
    def __init__(self, track, **kwargs):
        self.track = track
        super().__init__(**kwargs)