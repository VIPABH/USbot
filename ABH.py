from telethon import TelegramClient, events
import asyncio, os
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
ABH = TelegramClient('session', api_id, api_hash)
def ok(func):
    async def wrapper(event):
        uid = event.sender_id
        owner = (await event.client.get_me()).id
        if uid != owner:
            return
        await func(event)
    return wrapper
