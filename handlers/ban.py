# handlers/ban.py
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import BadRequest

from config import Settings

async def register_ban_handlers(dp):
    @dp.message_handler(commands=["ban"], is_chat_admin=True)
    async def ban_user(message: types.Message):
        if not message.reply_to_message:
            await message.reply("Reply to a message to ban the user!")
            return

        try:
            await message.chat.kick(
                user_id=message.reply_to_message.from_user.id,
                until_date=None
            )
            await message.reply(f"User {message.reply_to_message.from_user.mention} has been banned!")
        except BadRequest as e:
            await message.reply(f"Error: {e}")
