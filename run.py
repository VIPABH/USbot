from telethon import events
import asyncio
from config import *
from UScode import *
from التخزين import *
from ABH import *
from ذاتية import *
from ميمز import *
from امسح import *
from الردود import *
async def main():
    await ABH.start()  
    print("run is running")
    await config_vars()
    await ABH.run_until_disconnected()
asyncio.run(main())
