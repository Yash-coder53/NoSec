# handlers/gban.py
from aiogram import types
from aiogram.dispatcher import FSMContext

from config import Settings
from models.database import Database

db = Database()

async def register_gban_handlers(dp):
    @dp.message_handler(commands=["gban"], user_id=Settings.ADMIN_IDS)
    async def global_ban_user(message: types.Message):
        if not message.reply_to_message:
            await message.reply("Reply to a message to globally ban the user!")
            return

        user_id = message.reply_to_message.from_user.id
        await db.add_gban(user_id)
        await message.reply(f"User {message.reply_to_message.from_user.mention} has been globally banned!")
