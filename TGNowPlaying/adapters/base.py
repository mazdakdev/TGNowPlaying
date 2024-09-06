from abc import ABC, abstractmethod
from typing import Optional, Tuple

class ProviderAdapter(ABC):
    """
    Abstract base class for implementing provider adapters.

    Subclasses must override the `fetch_current_item` method to provide specific
    functionality for fetching data from different providers.

    The `fetch_current_item` method must return a tuple containing:
    - A string message to be sent to the channel.
    - A string title to be set for the channel's title.
    - An optional string URL for the profile image to be set on the channel.
    """

    @abstractmethod
    async def fetch_current_item(self) -> Optional[Tuple[str, str, str]]:
        pass
