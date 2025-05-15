import asyncio
from telethon import TelegramClient, events
import os
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
ABH = TelegramClient("bot", api_id, api_hash)
from config import *
from UScode import *
from التخزين import *
from ذاتية import *
from ميمز import *
from امسح import *
from الردود import *
async def main():
 print("✅ تم تشغيل البوت بنجاح.")
 if not await ABH.is_user_authorized():
  print("❌ البوت غير مفعل أو التوكن غير صحيح.")
  return
 await config_vars(events)
 await ABH.run_until_disconnected()
asyncio.run(main())
