# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split(",")))
    DATABASE_URL = os.getenv("DATABASE_URL")
    LOG_CHANNEL = os.getenv("LOG_CHANNEL")
    
    # Anti-spam settings
    MAX_WARNINGS = int(os.getenv("MAX_WARNINGS", 3))
    RAID_DETECTION_THRESHOLD = int(os.getenv("RAID_DETECTION_THRESHOLD", 5))
    RAID_TIME_WINDOW = int(os.getenv("RAID_TIME_WINDOW", 10))
