# models/database.py
import sqlite3
import logging
from typing import Optional, List

from utils.logger import setup_logger

logger = setup_logger(__name__)

class Database:
    def __init__(self, db_path: str = "database.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS gbans (
            user_id INTEGER PRIMARY KEY,
            reason TEXT,
            banned_by INTEGER,
            banned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        self.conn.commit()
    
    async def add_gban(self, user_id: int, reason: str = "", banned_by: int = 0):
        try:
            self.cursor.execute("""
            INSERT OR REPLACE INTO gbans (user_id, reason, banned_by)
            VALUES (?, ?, ?)
            """, (user_id, reason, banned_by))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Error adding gban: {e}")
            return False
    
    async def is_gbanned(self, user_id: int) -> bool:
        self.cursor.execute("SELECT 1 FROM gbans WHERE user_id = ?", (user_id,))
        return bool(self.cursor.fetchone())
    
    def close(self):
        self.conn.close()
