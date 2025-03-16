from kivymd.uix.list import TwoLineIconListItem

class PlaylistCard(TwoLineIconListItem):
    def __init__(self, playlist_id, **kwargs):
        self.playlist_id = playlist_id
        self.checkbox = False
        super().__init__(**kwargs)