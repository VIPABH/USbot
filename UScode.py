from telethon import TelegramClient, events
import asyncio, os
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
ABH = TelegramClient('session', int(api_id), api_hash)
@ABH.on(events.NewMessage(pattern='خاص'))
async def save(event):
    uid = event.sender_id
    me = await ABH.get_me()
    r = await event.get_reply_message()
    if not r:
        await event.edit('🤔 يجب أن ترد على رسالة.')
        await asyncio.sleep(3)
        await event.delete()
        return
    if uid == me.id:
          await r.forward_to(me.id)
          await asyncio.sleep(3)
          await event.delete()
    else:
        return
async def main():
    await ABH.start()
    await ABH.run_until_disconnected()
asyncio.run(main())
