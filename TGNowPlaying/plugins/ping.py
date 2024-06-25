from pyrogram import filters
from pyrogram.types import Message
from TGNowPlaying import bot
from TGNowPlaying import BotStartTime

@bot.on_message(filters.command("ping"))
async def ping(_ , message:Message):
    await message.reply("PONG; I'm here Mazdak.")