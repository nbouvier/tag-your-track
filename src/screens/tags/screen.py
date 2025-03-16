from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import OneLineIconListItem
import src.db as db
from src.screens.tags.create_dialog.component import CreateDialog
from src.screens.tags.tag_card.component import TagCard

class TagsScreen(MDScreen):
    def __init__(self, app, **kwargs):
        self.app = app
        self.create_dialog = CreateDialog(app, self.create_tag)
        super().__init__(**kwargs)
        
    def on_kv_post(self, base_widget):
        """Called after kv file is loaded"""
        self.refresh_tags()

    def refresh_tags(self):
        self.ids.tag_list.clear_widgets()
        
        tags = db.get_all_tags(self.app.db)
        for tag in tags:
            tag_card = TagCard(tag.id, tag.name, self.delete_tag)
            self.ids.tag_list.add_widget(tag_card)

    def create_tag(self, name):
        db.create_tag(self.app.db, name)
        self.refresh_tags()

    def update_tag(self, tag_id, new_name):
        db.update_tag(self.app.db, tag_id, new_name)
        self.refresh_tags()

    def delete_tag(self, tag_id):
        db.delete_tag(self.app.db, tag_id)
        self.refresh_tags()