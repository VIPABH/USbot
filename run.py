from telethon import events
from UScode import *
from config import *
from ABH import *
from التخزين import *
import asyncio
async def main():
    await ABH.start()
    print("run is running")
    await config_vars()
    await ABH.run_until_disconnected()
asyncio.run(main())
