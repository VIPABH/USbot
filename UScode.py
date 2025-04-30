from telethon import TelegramClient, events
import asyncio, os
from telethon.sessions import StringSession
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
session = 'session'
ABH = TelegramClient(session, int(api_id), api_hash)
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
          await event.delete()
          await r.forward_to(me.id)
    else:
        return
@ABH.on(events.NewMessage('.مسح'))
async def dele(event):
    await event.delete()
    r = await event.get_reply_message()
    await r.delete()
@ABH.on(events.NewMessage(pattern='جلسه'))
async def send_session_string(event):
    me = await ABH.get_me()
    session_string = ABH.session.save() 
    await ABH.send_message(me.id, f"🔐 Session String:\n`{session_string}`")
async def main():
    await ABH.start()
    await ABH.run_until_disconnected()
asyncio.run(main())
