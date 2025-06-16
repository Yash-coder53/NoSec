# utils/helpers.py
from aiogram import types
from config import Settings

def is_admin(user_id: int) -> bool:
    return user_id in Settings.ADMIN_IDS

async def delete_message(message: types.Message, delay: int = 0):
    """Delete a message after an optional delay."""
    try:
        await message.delete(delay=delay)
    except Exception as e:
        pass  # Message might be already deleted or we don't have permissions
