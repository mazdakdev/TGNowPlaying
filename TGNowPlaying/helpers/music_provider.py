from TGNowPlaying.helpers.providers.spotify import SpotifyAPI

class MusicProvider:
    def __init__(self):
        self.providers = {
            "spotify": SpotifyAPI(),
            # "apple_music": AppleMusicAPI()
        }

    def get_current_track(self, provider: str):
        if provider in self.providers:
            return self.providers[provider].get_current_track()
        else:
            raise ValueError("Unsupported Music Provider")
