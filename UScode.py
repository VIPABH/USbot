from telethon import TelegramClient, events
import asyncio, os
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
session = 'session'
ABH = TelegramClient(session, int(api_id), api_hash)
@ABH.on(events.NewMessage(pattern=r'^خاص$'))
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
@ABH.on(events.NewMessage(pattern=r'^؟؟$'))
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
@ABH.on(events.NewMessage(pattern=r'^رسالة (\S+) (.+)$'))
async def send(event):
    await event.delete()
    to = event.pattern_match.group(1)
    text = event.pattern_match.group(2)
    r = await event.get_reply_message()
    if r:
        abh = f'{to} {text}'
        to = r.sender_id
    await ABH.send_message(to, abh)
async def main():
    await ABH.start()
    await ABH.run_until_disconnected()
asyncio.run(main())
