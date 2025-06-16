# handlers/error.py
from aiogram import types
from aiogram.utils.exceptions import TelegramAPIError
import logging

from utils.logger import setup_logger

logger = setup_logger(__name__)

async def register_error_handlers(dp):
    @dp.errors_handler()
    async def errors_handler(update: types.Update, exception: TelegramAPIError):
        logger.error(f"Update: {update}\nException: {exception}", exc_info=True)
        
        if isinstance(exception, TelegramAPIError):
            return True  # Suppress the error
        
        return False
