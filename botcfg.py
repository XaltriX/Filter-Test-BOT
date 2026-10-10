"""
Runtime settings editable from /admin (saved in MongoDB, cached in memory).
    botcfg.get("daily_limit")          -> value (default from DEFAULTS)
    await botcfg.set("daily_limit", 5) -> saved + cache updated
Plain module (not a plugin) so there is exactly ONE shared cache.
"""
import copy
from info import DELETE_TIME

CFG_ID = -1   # document id in the bot_settings collection

DEFAULTS = {
    "daily_limit": 3,                 # free files per 24h
    "delete_extra_min": 15,           # free/verified: file length + this many minutes
    "delete_extra_min_premium": 45,   # premium: file length + this many minutes
    "delete_fallback_sec": DELETE_TIME,        # when file length is unknown (documents)
    "delete_fallback_sec_premium": 1800,
    "lock_free_forward": True,        # True = free (unverified) users cannot forward/save files
    "verify_on": True,
    "verify_hours": 3,                # access after one verification
    "verify_min_seconds": 20,         # faster than this = bypass attempt
    "shorteners": [],                 # [{id, site, api, tutorial, on}]
}

_cfg = {}


def get(key):
    return copy.deepcopy(_cfg[key] if key in _cfg else DEFAULTS[key])


async def set(key, value):
    from database.users_chats_db import db
    _cfg[key] = value
    await db.botcol.update_one({"id": CFG_ID}, {"$set": {f"cfg.{key}": value}}, upsert=True)


async def load():
    from database.users_chats_db import db
    doc = await db.botcol.find_one({"id": CFG_ID})
    _cfg.clear()
    _cfg.update((doc or {}).get("cfg", {}))
