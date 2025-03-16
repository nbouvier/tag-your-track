class Song:
    def __init__(self, data):
        self.data = data

    def get_id(self):
        return self.data['videoId']

    def get_title(self):
        return self.data['title']

    def get_artists(self):
        return ", ".join([a['name'] for a in self.data['artists']])
    
    def get_thumbnail(self):
        thumbnails = self.data['thumbnails']
        return thumbnails[0]['url'] if len(thumbnails) else ''
    
    def get_album(self):
        return self.data['album']
    
    def get_duration(self):
        return self.data['duration_seconds']