from telethon import TelegramClient, events
import asyncio, os
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
ABH = TelegramClient('session', api_id, api_hash)
@ABH.on(events.NewMessage(pattern='خاص'))
async def save(event):
    uid = event.sender_id
    me = await ABH.get_me()
    r = await event.get_reply_message()
    if not r:
        await event.edit('🤔')
        await asyncio.sleep(3)
        await event.delete()
    else:
       return
    if uid == me.id:
        await event.forward(me.id, r)
        await asyncio.sleep(3)
        await event.delete()
    else:
       return
ABH.run_until_disconnected()
