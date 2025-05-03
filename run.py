from telethon import events
from UScode import *
from config import * 
from ABH import *
from موارد import * 
import asyncio
async def main():
    await ABH.start()
    print("✅ البوت يعمل الآن")
    await ABH.run_until_disconnected()
asyncio.run(main())
