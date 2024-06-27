import asyncio
import requests
from io import BytesIO
from pyrogram import Client
from TGNowPlaying.helpers.utils import get_current_track
from TGNowPlaying.logging import LOGGER
from TGNowPlaying.settings import settings


async def periodic_task(app: Client, provider: str, channel_id: int):
    LOGGER(__name__).info("Starting predioc task....")
    while True:
        track_name, artist_name, track_image_url = get_current_track(provider)
        if track_name and artist_name and track_image_url:
            LOGGER(__name__).info(f"Updating channel with track: {track_name} by {artist_name}") 

            await app.set_chat_title(settings.CHANNEL_ID, f"{track_name} - {artist_name}")

            await app.delete_chat_photo(settings.CHANNEL_ID) # deletes the previous photo
            
            photo = BytesIO(requests.get(track_image_url).content)
            await app.set_chat_photo(chat_id=settings.CHANNEL_ID, photo=photo)
    
            await app.send_message(channel_id, f"Now Playing....")  
        
        await asyncio.sleep(300)  # Sleep for 5 minutes
