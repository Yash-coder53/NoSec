# bot.py
import asyncio
from aiogram import Bot, Dispatcher
from config import Settings
from handlers import register_all_handlers
from utils.logger import setup_logger

logger = setup_logger(__name__)

async def main():
    settings = Settings()
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher(bot)
    
    # Register handlers
    register_all_handlers(dp)
    
    try:
        logger.info("Starting bot...")
        await dp.start_polling()
    finally:
        await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
