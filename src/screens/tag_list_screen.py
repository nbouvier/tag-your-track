from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, OneLineIconListItem
from kivymd.uix.textfield import MDTextField
from sqlalchemy.orm import Session
from .. import db

class TagListScreen(MDScreen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.name = "tag_list"
        self.build()

    def build(self):
        layout = MDBoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header with back button and add button
        header = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=50
        )
        
        add_button = MDIconButton(
            icon="plus",
            on_release=self.show_create_dialog
        )
        
        header.add_widget(add_button)
        
        # Tag list
        self.tag_list = MDList()
        self.refresh_tags()
        
        layout.add_widget(header)
        layout.add_widget(self.tag_list)
        self.add_widget(layout)

    def refresh_tags(self):
        self.tag_list.clear_widgets()
        tags = db.get_all_tags(self.app.db)
        for tag in tags:
            item = OneLineIconListItem(
                text=tag.name,
                on_release=lambda x, t=tag: self.edit_tag(t)
            )
            delete_button = MDIconButton(
                icon="trash-can",
                on_release=lambda x, t=tag: self.delete_tag(t)
            )
            item.add_widget(delete_button)
            self.tag_list.add_widget(item)

    def show_create_dialog(self, *args):
        self.dialog = MDDialog(
            title="Create New Tag",
            type="custom",
            content_cls=MDTextField(
                hint_text="Tag name"
            ),
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_release=lambda x: self.dialog.dismiss()
                ),
                MDFlatButton(
                    text="CREATE",
                    on_release=self.create_tag
                ),
            ],
        )
        self.dialog.open()

    def create_tag(self, *args):
        name = self.dialog.content_cls.text
        if name:
            self.add_tag(name)
        self.dialog.dismiss()

    def add_tag(self, name):
        db.create_tag(self.app.db, name)
        self.refresh_tags()

    def delete_tag(self, tag):
        db.delete_tag(self.app.db, tag.id)
        self.refresh_tags()

    def edit_tag(self, tag):
        # TODO: Implement tag editing if needed
        pass

    def update_tag(self, tag_id, new_name):
        db.update_tag(self.app.db, tag_id, new_name)
        self.refresh_tags()
