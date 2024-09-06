from pyrogram import filters
from pyrogram.types import Message
from TGNowPlaying import bot
from TGNowPlaying.tasks import task_scheduler
from TGNowPlaying.settings import settings
from TGNowPlaying.logging import LOGGER

"""
Start listening on a provider task.
cmd: /listen_on <provider>
"""
@bot.on_message(filters.command(["listen_on"]))
async def listen_on(_, message: Message):
    LOGGER(__name__).info("Received /listen_on command")

    if len(message.command) < 2:
        await message.reply("Please specify a provider, use: /listen_on <provider_name>")
        return

    provider = message.command[1]
    task_scheduler.schedule_task(bot, provider, settings.CHANNEL_ID)
    await message.reply(f"")

"""
Cancels the current provider listening task.
cmd: /cancel
"""
@bot.on_message(filters.command(["cancel"]))
async def cancel_listening(_, message: Message):
    LOGGER(__name__).info("Received /cancel command")

    if task_scheduler.current_task:
        task_scheduler.cancel_task()
        await message.reply("Stopped listening to the current provider.")
    else:
        await message.reply("No active listening task to cancel.")
