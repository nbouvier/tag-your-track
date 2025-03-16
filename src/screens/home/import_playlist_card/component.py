from kivymd.uix.card import MDCard

class ImportPlaylistCard(MDCard):
    def __init__(self, playlist_id, title, tracks, **kwargs):
        self.playlist_id = playlist_id
        self.title = title
        self.tracks = tracks
        self.checkbox = None
        super().__init__(**kwargs)