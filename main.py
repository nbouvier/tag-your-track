from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from src.database import Session
from src.screens.main_screen import MainScreen
from src.screens.tag_list_screen import TagListScreen
from ytmusicapi import YTMusic

class TagYourTracks(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Session()
        self.ytmusic = YTMusic("./browser.json")
        self.screen_manager = MDScreenManager()
        self.bottom_navigation = MDBottomNavigation()

    def build(self):
        # Create bottom navigation items
        home_item = MDBottomNavigationItem(name='home', text='Home', icon='home')
        home_item.add_widget(MainScreen(self))

        tags_item = MDBottomNavigationItem(name='tags', text='Tags', icon='tag')
        tags_item.add_widget(TagListScreen(self))

        # Add items to bottom navigation
        self.bottom_navigation.add_widget(home_item)
        self.bottom_navigation.add_widget(tags_item)

        return self.bottom_navigation

    def on_stop(self):
        if self.db:
            self.db.close()
            Session.remove()

if __name__ == '__main__':
    TagYourTracks().run()
