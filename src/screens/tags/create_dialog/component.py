from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class CreateDialog(MDDialog):
    def __init__(self, app, create_tag_callback, **kwargs):
        self.app = app
        self.create_tag_callback = create_tag_callback

        buttons=[
            MDFlatButton(text="Cancel", on_release=lambda x: self.dismiss()),
            MDFlatButton(text="Create", on_release=self.create_tag),
        ]
        super().__init__(buttons=buttons, auto_dismiss=False, **kwargs)

    def create_tag(self, *args):
        name = self.ids.name_input.text
        if name:
            self.create_tag_callback(name)
            self.dismiss()