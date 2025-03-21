from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
import src.db as db
from src.screens.home.import_dialog.component import ImportDialog
from src.screens.home.track_card.component import TrackCard

class HomeScreen(MDScreen):
    def __init__(self, app, **kwargs):
        self.app = app
        self.import_dialog = ImportDialog(app, self.import_playlist)
        super().__init__(**kwargs)
        
    def on_kv_post(self, base_widget):
        """Called after kv file is loaded"""
        self.load_tags()
        self.load_tracks()

    def load_tags(self):
        self.tags = db.get_all_tags(self.app.db)

    def load_tracks(self):
        self.ids.tracks_container.clear_widgets()
        for track in self.app.playlist.get_tracks():
            track_card = TrackCard(track)
            self.ids.tracks_container.add_widget(track_card)

    def on_pre_enter(self, *args):
        """Called when screen is about to be entered"""
        self.load_tags()
    
    def open_tag_list(self, instance, value):
        if value:
            self.create_tag_list()
            self.tag_list.open()

    def create_tag_list(self):
        items = [
            {
                "text": tag.name,
                "viewclass": "OneLineListItem", 
                "on_release": lambda x=tag.name: self.on_tag_select(x)
            } for tag in self.tags
        ]

        self.tag_list = MDDropdownMenu(
            caller=self.ids.tag_field,
            items=items,
        )
    
    def on_tag_select(self, tag_name):
        self.ids.tag_field.text = tag_name
        self.tag_list.dismiss()
        # TODO: Filter tracks by selected tag

    def import_playlist(self, playlist):
        track_ids = []
        for track in playlist.get_tracks():
            (_, created) = db.create_track_if_not_exists(
                self.app.db,
                youtube_id=track.get_id(),
                title=track.get_title(),
                artist=track.get_artists()
            )
            if created:
                track_ids.append(track['videoId'])

        if track_ids:
            self.app.ytmusic.add_playlist_items(self.app.playlist_id, videoIds=track_ids)
            self.load_tracks()