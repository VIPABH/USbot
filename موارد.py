from telethon import TelegramClient, events
import asyncio, os, UScode
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
session = 'session'
ABH = TelegramClient(session, int(api_id), api_hash)
def ok(func):
    async def wrapper(event):
        uid = event.sender_id
        owner = (await event.ABH.get_me()).id
        if uid != owner:
            return
        await func(event)
    return wrapper
async def main():
    await ABH.start()
    await ABH.run_until_disconnected()
print("usbot is running ◉")
asyncio.run(main())
