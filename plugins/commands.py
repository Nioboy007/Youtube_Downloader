from pyrogram.types import Message
from pyrogram import Client, filters

@Client.on_message(filters.private & filters.command(['start', 'help']))
async def start_bot(bot, m: Message):
    await m.reply_text("You have started this bot.")
