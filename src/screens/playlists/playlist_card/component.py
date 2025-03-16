from kivymd.uix.card import MDCard

class PlaylistCard(MDCard):
    def __init__(self, playlist_id, title, thumbnail_url, on_release_callback, **kwargs):
        self.playlist_id = playlist_id
        self.title = title
        self.thumbnail_url = thumbnail_url
        self.on_release_callback = on_release_callback
        super().__init__(**kwargs)