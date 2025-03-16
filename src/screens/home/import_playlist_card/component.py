from kivymd.uix.list import ThreeLineAvatarIconListItem

class ImportPlaylistCard(ThreeLineAvatarIconListItem):
    def __init__(self, playlist_id, title, tracks, thumbnail, on_import_callback, **kwargs):
        self.playlist_id = playlist_id
        self.title = title
        self.tracks = tracks
        self.thumbnail = thumbnail
        self.on_import_callback = on_import_callback
        super().__init__(**kwargs)