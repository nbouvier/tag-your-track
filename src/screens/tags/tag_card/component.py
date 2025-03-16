from kivymd.uix.card import MDCard

class TagCard(MDCard):
    def __init__(self, tag_id, name, delete_tag_callback, **kwargs):
        self.tag_id = tag_id
        self.name = name
        self.delete_tag_callback = delete_tag_callback
        super().__init__(**kwargs)