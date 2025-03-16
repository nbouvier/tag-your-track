from kivymd.uix.list import ThreeLineAvatarIconListItem

class ImportPlaylistCard(ThreeLineAvatarIconListItem):
    def __init__(self, playlist, on_import_callback, **kwargs):
        self.playlist = playlist
        self.on_import_callback = on_import_callback
        super().__init__(**kwargs)