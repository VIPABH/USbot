from telethon import events
import asyncio
async def main():
    await config_vars(events)
    await ABH.start()
    print("run is running")
    await ABH.run_until_disconnected()
from config import *
from UScode import *
from التخزين import *
from ABH import *
from ذاتية import *
from ميمز import *
from امسح import *
from الردود import *
asyncio.run(main())
