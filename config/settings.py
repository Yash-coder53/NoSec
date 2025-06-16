import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Bot Token
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    # Admin IDs (comma separated)
    ADMIN_IDS = [int(id) for id in os.getenv('ADMIN_IDS', '').split(',') if id]
    
    # Sudo Users (super admins with extra privileges)
    SUDO_IDS = [int(id) for id in os.getenv('SUDO_IDS', '').split(',') if id]
    
    # Database settings
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
    DB_NAME = os.getenv('DB_NAME', 'NoToSectBot')
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'bot.log')
    
    # Ban settings
    MAX_BAN_REASON_LENGTH = 200
    BAN_COOLDOWN = 3600  # 1 hour in seconds
    
    # Anti-raid settings
    RAID_THRESHOLD = 5  # Number of joins in short time to trigger
    RAID_TIME_WINDOW = 60  # Seconds to monitor for raid detection
    
    # Rate limiting
    COMMAND_RATE_LIMIT = 3  # Commands per second
    BAN_RATE_LIMIT = 2  # Bans per minute
