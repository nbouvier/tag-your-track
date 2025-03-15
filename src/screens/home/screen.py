from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.textfield import MDTextField
from src.classes.song import Song
import src.db as db
from src.models import Tag

class Home(MDScreen):
    def __init__(self, app, **kwargs):
        self.app = app
        super().__init__(**kwargs)
        
    def on_kv_post(self, base_widget):
        """Called after kv file is loaded"""
        self.load_tags()
        self.load_songs()

    def load_tags(self):
        self.tags = db.get_all_tags(self.app.db)

    def load_songs(self):
        self.ids.songs_container.clear_widgets()

        songs = self.app.ytmusic.get_playlist(self.app.playlist_id)['tracks']
        for song in songs:
            song_layout = Song(
                title=song['title'],
                artist=song.get('artists', [{'name': 'Unknown'}])[0]['name']
            ).build()
            self.ids.songs_container.add_widget(song_layout)

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
        # TODO: Filter songs by selected tag