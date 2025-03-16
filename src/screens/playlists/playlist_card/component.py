from kivymd.uix.list import TwoLineAvatarListItem

class PlaylistCard(TwoLineAvatarListItem):
    def __init__(self, playlist_id, title, tracks, thumbnail, on_release_callback, **kwargs):
        self.playlist_id = playlist_id
        self.title = title
        self.tracks = tracks
        self.thumbnail = thumbnail
        self.on_release_callback = on_release_callback
        super().__init__(**kwargs)