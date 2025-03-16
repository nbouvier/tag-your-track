from kivymd.uix.list import TwoLineAvatarListItem

class PlaylistCard(TwoLineAvatarListItem):
    def __init__(self, playlist, on_release_callback, **kwargs):
        self.playlist = playlist
        self.on_release_callback = on_release_callback
        super().__init__(**kwargs)