from kivymd.uix.list import ThreeLineAvatarIconListItem

class PlaylistSongCard(ThreeLineAvatarIconListItem):
    def __init__(self, track, **kwargs):
        self.track = track
        super().__init__(**kwargs)