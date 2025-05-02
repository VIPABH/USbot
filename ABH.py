from telethon import TelegramClient, events
import asyncio, os
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
ABH = TelegramClient('session', api_id, api_hash)
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
    print("البرنامج يعمل... اضغط Ctrl+C للإيقاف.")
    await ABH.run_until_disconnected()
    import UScode, التخزين, run #type: ignore
asyncio.run(main())
