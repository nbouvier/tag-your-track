from kivymd.uix.list import ThreeLineAvatarIconListItem

class TrackCard(ThreeLineAvatarIconListItem):
    def __init__(self, track, **kwargs):
        self.track = track
        super().__init__(**kwargs)