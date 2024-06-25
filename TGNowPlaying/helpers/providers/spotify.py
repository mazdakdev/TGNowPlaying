import spotipy
from spotipy.oauth2 import SpotifyOAuth
from TGNowPlaying.settings import settings

class SpotifyAPI:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=settings.SPOTIFY_CLIENT_ID,
            client_secret=settings.SPOTIFY_CLIENT_SECRET,
            redirect_uri=settings.SPOTIFY_REDIRECT_URI,
            scope="user-read-playback-state"
        ))

    def get_current_track(self):
        current_playback = self.sp.current_playback()
        if current_playback and current_playback['is_playing']:
            return current_playback 
        return None
