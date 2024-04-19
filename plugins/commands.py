from presets import Presets
from pyrogram.types import Message
from pyrogram import Client, filters

@Client.on_message(filters.private & filters.command(['start', 'help']))
async def start_bot(bot, m: Message):
    await m.reply_text(Presets.WELCOME_MSG.format(m.from_user.first_name))
