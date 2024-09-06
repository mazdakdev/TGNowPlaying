from TGNowPlaying.adapters.base import ProviderAdapter
from typing import Optional, Tuple
from TGNowPlaying.settings import settings
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import logging

class SpotifyAdapter(ProviderAdapter):
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=settings.SPOTIFY_CLIENT_ID,
            client_secret=settings.SPOTIFY_CLIENT_SECRET,
            redirect_uri=settings.SPOTIFY_REDIRECT_URI,
            scope="user-read-playback-state"
        ))

    async def fetch_current_item(self) -> Optional[Tuple[str, str, str]]:
        try:
            current_playback = self.sp.current_playback()
        except spotipy.SpotifyException as e:
            logging.getLogger(__name__).error(f"Spotify API error: {e}")
            return None

        if current_playback and current_playback['is_playing']:
            track = current_playback['item']

            track_name = track['name']
            artist_name = ', '.join(artist['name'] for artist in track['artists'])
            image = track['album']['images'][0]['url'] if track['album']['images'] else ""

            title = f"{track_name} - {artist_name}"
            message = f"Currently playing: {track_name} by {artist_name}"

            return title, message, image

        return None
