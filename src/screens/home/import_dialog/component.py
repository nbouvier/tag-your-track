from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from ..import_playlist_card.component import ImportPlaylistCard

class ImportDialog(MDDialog):
    def __init__(self, app, on_import_callback, **kwargs):
        self.app = app
        self.on_import_callback = on_import_callback

        buttons = [MDFlatButton(text="Close", on_release=lambda x: self.dismiss())]
        super().__init__(buttons=buttons, auto_dismiss=False, **kwargs)
        
    def on_pre_open(self):
        self.ids.playlist_list.clear_widgets()
        for playlist in self.app.playlists:
            playlist_card = ImportPlaylistCard(playlist, self.on_import_callback)
            self.ids.playlist_list.add_widget(playlist_card)
    
        # Bug fixing dialog height
        height = Window.height * 0.7
        self.children[1].children[2].height = height
        self.height = height