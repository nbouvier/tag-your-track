from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
from api.main import Api

class TagManagement:
    def __init__(self):
        self.tags = []
        self.selected_tags = []
        self.fetch_tags()

    def fetch_tags(self):
        self.tags = Api.get_tags()

    def build(self):
        layout = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=50,
            padding=10,
            spacing=10
        )

        self.tag_button = MDFlatButton(
            text="Select Tags",
            size_hint=(None, None),
            height=40
        )

        self.create_menu()
        self.tag_button.bind(on_release=self.open_menu)
        layout.add_widget(self.tag_button)

        return layout

    def create_menu(self):
        menu_items = [
            {
                "text": f"{'✓ ' if tag['id'] in [t['id'] for t in self.selected_tags] else '  '}{tag['name']}",
                "viewclass": "OneLineListItem",
                "height": 50,
                "on_release": lambda x=tag: self.toggle_tag(x),
            } for tag in self.tags
        ]

        self.dropdown = MDDropdownMenu(
            caller=self.tag_button,
            items=menu_items,
            width_mult=4,
            max_height=250,
        )

    def open_menu(self, *args):
        self.create_menu()  # Recreate menu with updated items
        self.dropdown.open()

    def toggle_tag(self, tag):
        tag_ids = [t['id'] for t in self.selected_tags]
        if tag['id'] in tag_ids:
            self.selected_tags = [t for t in self.selected_tags if t['id'] != tag['id']]
        else:
            self.selected_tags.append(tag)
        
        if not self.selected_tags:
            self.tag_button.text = "Select Tags"
        else:
            self.tag_button.text = f"Tags: {', '.join(t['name'] for t in self.selected_tags)}"
        
        self.dropdown.dismiss()  # Dismiss the current menu
        self.create_menu()  # Create new menu with updated items
        self.dropdown.open()  # Reopen the menu
