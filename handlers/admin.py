# handlers/admin.py
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from config import Settings

async def register_admin_handlers(dp):
    @dp.message_handler(Command("admin"), user_id=Settings.ADMIN_IDS)
    async def admin_panel(message: types.Message):
        await message.answer("Admin panel:\n"
                           "/stats - Bot statistics\n"
                           "/broadcast - Send message to all users")

    @dp.message_handler(Command("stats"), user_id=Settings.ADMIN_IDS)
    async def show_stats(message: types.Message):
        # Implement stats logic here
        await message.answer("Bot statistics: ...")
