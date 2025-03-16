from kivymd.uix.list import TwoLineAvatarIconListItem

class TagCard(TwoLineAvatarIconListItem):
    def __init__(self, tag_id, name, on_delete_callback, **kwargs):
        self.tag_id = tag_id
        self.name = name
        self.on_delete_callback = on_delete_callback
        super().__init__(**kwargs)