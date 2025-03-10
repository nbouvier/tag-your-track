from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu

class TagManagement:
    def __init__(self):
        self.dummy_tags = ["Rock", "Jazz", "Classical", "Pop", "Metal"]
        self.selected_tags = []

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
                "text": f"{'✓ ' if tag in self.selected_tags else '  '}{tag}",
                "viewclass": "OneLineListItem",
                "height": 50,
                "on_release": lambda x=tag: self.toggle_tag(x),
            } for tag in self.dummy_tags
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
        if tag in self.selected_tags:
            self.selected_tags.remove(tag)
        else:
            self.selected_tags.append(tag)
        
        if not self.selected_tags:
            self.tag_button.text = "Select Tags"
        else:
            self.tag_button.text = f"Tags: {', '.join(self.selected_tags)}"
        
        self.dropdown.dismiss()  # Dismiss the current menu
        self.create_menu()  # Create new menu with updated items
        self.dropdown.open()  # Reopen the menu
