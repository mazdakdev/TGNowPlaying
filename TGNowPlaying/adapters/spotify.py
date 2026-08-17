from TGNowPlaying.adapters.base import ProviderAdapter
from typing import Optional, Tuple
from TGNowPlaying.settings import settings
from spotipy.oauth2 import SpotifyOAuth
import subprocess
import asyncio
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
            message = f"Now listening to..."

            return title, message, image

        return None

class SpotifyLocalAdapter(ProviderAdapter):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    async def fetch_current_item(self) -> Optional[Tuple[str, str, str]]:
        script = '''
        tell application "Spotify"
            if player state is playing then
                set trackName to name of current track
                set artistName to artist of current track
                set artworkURL to artwork url of current track
                return trackName & "|||" & artistName & "|||" & artworkURL
            end if
        end tell
        '''

        try:
            result = await asyncio.to_thread(
                subprocess.run,
                ["osascript", "-e", script],
                capture_output=True,
                text=True,
                check=True,
            )

            output = result.stdout.strip()

            if not output:
                return None

            track_name, artist_name, image = output.split("|||", 2)

            title = f"{track_name} - {artist_name}"
            message = "Now listening to..."

            return title, message, image

        except subprocess.CalledProcessError as e:
            self.logger.error(f"Spotify local error: {e.stderr.strip()}")
            return None

        except ValueError:
            self.logger.error(
                f"Unexpected Spotify output: {result.stdout!r}"
            )
            return None

        except Exception as e:
            self.logger.error(f"Spotify local adapter error: {e}")
            return None