from telethon import TelegramClient, events
import asyncio, os
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
@ABH.on(events.NewMessage(pattern=r'^.مسح (\d+)$'))
async def dele(event):
    num = int(event.pattern_match.group(1)) + 1
    r = await event.get_reply_message()
    if r:
        await event.delete()
        await r.delete()
    else:
        for i in range(int(num)):
            async for msg in ABH.iter_messages(event.chat_id, limit=1):
                await msg.delete()
        await event.delete()
@ABH.on(events.NewMessage(pattern='؟؟؟'))
async def edit(event):
    await event.edit('`|`')
    await asyncio.sleep(0.4)
    await event.edit('`/`')
    await asyncio.sleep(0.4)
    await event.edit('`-`')
    await asyncio.sleep(0.4)
    await event.edit("`\`")
    await asyncio.sleep(0.4)
    await event.edit('`|`')
    await asyncio.sleep(0.4)
    await event.edit('`/`')
    await asyncio.sleep(0.4)
    await event.edit('`-`')
    await asyncio.sleep(0.4)
    await event.edit("`\`")
    await asyncio.sleep(0.4)
    await event.edit('`|`')
    await asyncio.sleep(0.4)
    await event.edit('`/`')
    await asyncio.sleep(0.4)
    await event.edit('`-`')
    await asyncio.sleep(0.4)
    await event.edit("`\`")
async def main():
    await ABH.start()
    await ABH.run_until_disconnected()
asyncio.run(main())
