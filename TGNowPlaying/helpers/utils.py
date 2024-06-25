from TGNowPlaying.helpers.music_provider import MusicProvider
from TGNowPlaying.logging import LOGGER

music_provider = MusicProvider()

def get_current_track(provider: str):
    LOGGER(__name__).info(f"Fetching current track for provider: {provider}")
    track_details = music_provider.get_current_track(provider)
    if track_details:
        track_name = track_details['item']['name']
        artist_name = track_details['item']['artists'][0]['name']  
        track_image_url = track_details['item']['album']['images'][0]['url']  
        LOGGER(__name__).info(f"Track found: {track_name} by {artist_name}, Image URL: {track_image_url}")  
        return track_name, artist_name, track_image_url

    LOGGER(__name__).error("No track details found") 
    return None, None, None


