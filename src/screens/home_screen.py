from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.textfield import MDTextField
from src.components.songs import Songs
from src.db import get_all_tags
from src.models import Tag

class HomeScreen(MDScreen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.name = 'home'
        self.build_layout()

    def build_layout(self):
        self.layout = MDBoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Create tag selector field
        self.tag_field = MDTextField(
            text="Select Tag",
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint_x=0.8,
            readonly=True
        )
        self.tag_field.bind(on_focus=self.open_tag_menu)
        
        # Get tags from DB and create menu
        tags = get_all_tags(self.app.db)
        self.tags_menu = MDDropdownMenu(
            caller=self.tag_field,
            items=[{"text": tag.name, "viewclass": "OneLineListItem", 
                   "on_release": lambda x=tag.name: self.on_tag_select(x)} 
                  for tag in tags],
            width_mult=4,
        )
        
        # Add field to layout
        self.layout.add_widget(self.tag_field)
        
        # Songs container
        self.songs_container = MDBoxLayout(orientation='vertical')
        scroll = MDScrollView()
        scroll.add_widget(self.songs_container)
        self.layout.add_widget(scroll)
        
        self.add_widget(self.layout)
        self.load_songs()
    
    def open_tag_menu(self, instance, value):
        if value:
            self.tags_menu.open()
    
    def load_songs(self):
        if hasattr(self.app, 'playlist_id'):
            songs = Songs(self.app.ytmusic, self.app.playlist_id)
            self.songs_container.clear_widgets()
            self.songs_container.add_widget(songs.build())
    
    def on_tag_select(self, tag_name):
        self.tag_field.text = tag_name
        self.tags_menu.dismiss()
        # TODO: Filter songs by selected tag

    def on_enter(self):
        """Called when screen is entered - refresh tags"""
        self.refresh_tags()
        self.load_songs()
    
    def refresh_tags(self):
        """Refresh the tags in the dropdown menu"""
        tags = get_all_tags(self.app.db)
        self.tags_menu = MDDropdownMenu(
            caller=self.tag_field,
            items=[{
                "text": tag.name,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=tag.name: self.on_tag_select(x)
            } for tag in tags],
            width_mult=4,
        )
