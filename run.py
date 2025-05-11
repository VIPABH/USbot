from telethon import events
from config import *
from UScode import *
from التخزين import *
from ABH import *
from ذاتية import *
from ميمز import *
from امسح import *
from الردود import *
import asyncio
async def main():
    await ABH.start()
    print("run is running")
    await config_vars(events)
    await ABH.run_until_disconnected()
asyncio.run(main())
