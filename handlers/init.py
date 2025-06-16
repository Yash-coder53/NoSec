# handlers/__init__.py
from .admin import register_admin_handlers
from .ban import register_ban_handlers
from .gban import register_gban_handlers
from .raid import register_raid_handlers
from .error import register_error_handlers

def register_all_handlers(dp):
    register_admin_handlers(dp)
    register_ban_handlers(dp)
    register_gban_handlers(dp)
    register_raid_handlers(dp)
    register_error_handlers(dp)
