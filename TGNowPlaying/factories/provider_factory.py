from typing import Type
from TGNowPlaying.adapters.spotify import SpotifyAdapter, SpotifyLocalAdapter
from TGNowPlaying.adapters.base import ProviderAdapter

class ProviderAdapterFactory:
    _adapters = {
        "spotify": SpotifyAdapter,
        "spotify-local": SpotifyLocalAdapter,
    }

    @staticmethod
    def get_adapter(provider_name: str) -> ProviderAdapter:
        adapter_cls = ProviderAdapterFactory._adapters.get(provider_name)
        if not adapter_cls:
            raise ValueError(f"Unknown provider: {provider_name}")

        return adapter_cls()