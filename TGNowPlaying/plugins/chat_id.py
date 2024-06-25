from pyrogram import filters
from pyrogram.types import Message
from TGNowPlaying import bot
from TGNowPlaying import BotStartTime

@bot.on_message(filters.command("chat_id"))
async def ping(_ , message:Message):
    await message.reply(f"Here is the chat_id: {message.chat.id}")