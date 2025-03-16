from .song import Song

class Playlist:
    def __init__(self, data, ytmusic=None, loaded=False):
        self.ytmusic = ytmusic
        self.data = data
        self.loaded = loaded

    def load(self):
        self.data = self.ytmusic.get_playlist(self.get_id())
        self.tracks = [Song(s) for s in self.data['tracks']]
        self.loaded = True

    def get_id(self):
        return self.data['playlistId']

    def get_title(self):
        return self.data['title']

    def get_artists(self):
        if not self.loaded:
            self.load()

        return ", ".join([a['name'] for a in self.data['artists']])
    
    def get_thumbnail(self):
        thumbnails = self.data['thumbnails']
        return thumbnails[0]['url'] if len(thumbnails) else ''
    
    def get_track_count(self):
        return str(self.data['trackCount']) if self.loaded else self.data['count']
    
    def get_tracks(self):
        if not self.loaded:
            self.load()
            
        return self.tracks
    
    def get_duration(self):
        if not self.loaded:
            self.load()

        return self.data['duration_seconds']