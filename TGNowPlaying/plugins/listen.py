"""
Plugin that listens for music change
"""

from pyrogram import filters
from pyrogram.types import Message
from TGNowPlaying import bot
from TGNowPlaying import BotStartTime
from TGNowPlaying.tasks import periodic_task
from TGNowPlaying.settings import settings
from TGNowPlaying.logging import LOGGER
import asyncio
from io import BytesIO
import requests


current_task = None

"""
Start listening on spotiy task.
cmd: /listen_on_spotify
"""
@bot.on_message(filters.command("listen_on_spotify"))
async def listen_on_spotify(_, message: Message):
    global current_task
    LOGGER(__name__).info("Received /listen_on_spotify command") 

    if current_task:
        current_task.cancel()

        LOGGER(__name__).info("Canceled existing task") 

    current_task = asyncio.create_task(periodic_task(bot, "spotify", settings.CHANNEL_ID))
    LOGGER(__name__).info("Started listening to Spotify and updating channel")


"""
Cancels all listening tasks.
cmd: /cancel
"""
@bot.on_message(filters.command("cancel"))
async def cancel_listening(_, message: Message):
    global current_task
    LOGGER(__name__).info("Received /cancel command") 

    if current_task:
        current_task.cancel()
        current_task = None
        await message.reply("Stopped listening to music.")
    else:
        await message.reply("No listening task to cancel.")
       
