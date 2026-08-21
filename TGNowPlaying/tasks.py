from TGNowPlaying.factories.provider_factory import ProviderAdapterFactory
from TGNowPlaying.logging import LOGGER
from pyrogram.client import Client
from typing import Tuple, Optional
from io import BytesIO
import asyncio
import httpx

class TaskScheduler:
    def __init__(self):
        self.current_task = None
        self.current_provider = None

    def schedule_task(self, app: Client, provider: str, channel_id: int, interval: int = 300):
        if self.current_task:
            self.cancel_task()

        async def periodic_update():
            while True:
                try:
                    await self.update_channel(app, provider, channel_id)
                except asyncio.CancelledError:
                    raise
                except Exception as e:
                    LOGGER(__name__).error(f"Error in periodic task for {provider}: {e}")
                await asyncio.sleep(interval)

        self.current_task = asyncio.create_task(periodic_update())
        self.current_provider = provider
        LOGGER(__name__).info(f"Started periodic task for {provider}")

    def cancel_task(self):
        if self.current_task:
            self.current_task.cancel()
            LOGGER(__name__).info(f"Stopped periodic task for {self.current_provider}")
            self.current_task = None
            self.current_provider = None

    @staticmethod
    async def update_channel(app: Client, provider: str, channel_id: int) -> None:
        adapter = ProviderAdapterFactory.get_adapter(provider)
        current_item = await adapter.fetch_current_item()

        if current_item:
            title, message, image = current_item
            LOGGER(__name__).info(f"Updating channel with track: {title}")

            await app.set_chat_title(channel_id, title)

            if image:
                try:
                    async with httpx.AsyncClient(timeout=10.0) as client:
                        response = await client.get(image)
                        response.raise_for_status()
                    photo = BytesIO(response.content)
                    photo.name = "cover.jpg"
                    await app.set_chat_photo(channel_id, photo=photo)
                except httpx.HTTPError as e:
                    LOGGER(__name__).warning(f"Failed to fetch track image: {e}")

            await app.send_message(channel_id, message)

task_scheduler = TaskScheduler()
