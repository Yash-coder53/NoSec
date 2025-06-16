# handlers/raid.py
from aiogram import types
from aiogram.dispatcher import FSMContext
from datetime import datetime, timedelta

from config import Settings
from models.database import Database

db = Database()

class RaidProtection:
    def __init__(self):
        self.user_join_times = {}

    async def check_raid(self, user_id: int, chat_id: int) -> bool:
        now = datetime.now()
        if user_id not in self.user_join_times:
            self.user_join_times[user_id] = []
        
        self.user_join_times[user_id].append(now)
        
        # Filter joins within the time window
        recent_joins = [t for t in self.user_join_times[user_id] 
                       if now - t < timedelta(seconds=Settings.RAID_TIME_WINDOW)]
        
        if len(recent_joins) >= Settings.RAID_DETECTION_THRESHOLD:
            return True
        return False

raid_protection = RaidProtection()

async def register_raid_handlers(dp):
    @dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
    async def new_members_handler(message: types.Message):
        for new_member in message.new_chat_members:
            if await raid_protection.check_raid(new_member.id, message.chat.id):
                await message.chat.kick(user_id=new_member.id)
                await message.answer(f"User {new_member.mention} was kicked for possible raid activity!")
