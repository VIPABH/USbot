from telethon import TelegramClient, events
import asyncio, os
from موارد import th
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
@ok
@ABH.on(events.NewMessage(pattern=r'^.تثبيت$'))
async def pin(event):
    await event.delete()
    gid = event.chat_id
    r = await event.get_reply_message()
    await ABH.pin_message(gid, r.id)
@ok
@ABH.on(events.NewMessage(pattern=r'^الغاء تثبيت$'))
async def pin(event):
    await event.delete()
    gid = event.chat_id
    r = await event.get_reply_message()
    await ABH.unpin_message(gid, r.id)
@ok
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
@ok
@ABH.on(events.NewMessage(pattern=r'^.مسح(?: (\d+))?$'))
async def dele(event):
    r = await event.get_reply_message()
    if r:
        await event.delete()
        await r.delete()
    else:
         num = int(event.pattern_match.group(1))
         messages = []
         async for msg in ABH.iter_messages(event.chat_id, limit=num + 1):
              messages.append(msg.id)
              await ABH.delete_messages(event.chat_id, messages)
@ok
@ABH.on(events.NewMessage(pattern=r'^؟؟$'))
async def edit(event):
    for i in range(5):
        await event.edit('`|`')
        await asyncio.sleep(0.4)
        await event.edit('`/`')
        await asyncio.sleep(0.4)
        await event.edit('`-`')
        await asyncio.sleep(0.4)
        await event.edit("`\`")
        await asyncio.sleep(0.4)
@ok
@ABH.on(events.NewMessage(pattern=r'^رسالة (\S+) (.+)$'))
async def send(event):
    r = await event.get_reply_message()
    if r:
         await event.delete()
         to = r.sender_id
         t1 = event.event.pattern_match(1)
         txt = event.event.pattern_match(2)
         text = f"{t1} {txt}"
         entity = await ABH.get_input_entity(to)
         await ABH.send_message(entity, text)
    else:
        await event.delete()
        to = event.pattern_match.group(1)
        text = event.pattern_match.group(2)
        entity = await ABH.get_input_entity(to)
        await ABH.send_message(entity, text)
@ok
@ABH.on(events.NewMessage(pattern=r'^وقتي (\d+)\s+(.+)$'))
async def timi(event):
    await event.delete()
    t = int(event.pattern_match.group(1))
    m = event.pattern_match.group(2)
    r = await event.get_reply_message()
    if r:
        await event.delete()
        msg = await r.reply(f'{m}')
        await asyncio.sleep(t)
        await msg.delete()
    else:
        msg2 = await event.respond(f'{m}')
        await asyncio.sleep(t)
        await msg2.delete()
@ok
@ABH.on(events.NewMessage(pattern=r'^.مسح رسائلي$'))
async def dele(event):
    try:
        owner = (await ABH.get_me()).id
        await event.delete()
        async for msg in ABH.iter_messages(event.chat_id, from_user=owner):
            await msg.delete()
    except Exception as e:
        await event.reply(f"حدث خطأ أثناء محاولة حذف الرسائل:\n{e}")
@ok
@ABH.on(events.NewMessage(pattern=r'^.مسح مشاركاته$'))
async def dele(event):
    r = await event.get_reply_message()
    if not r:
        await event.edit('🤔 يجب أن ترد على رسالة.')
        await asyncio.sleep(3)
        await event.delete()
        return
    owner = r.sender_id
    await event.delete()
    async for msg in ABH.iter_messages(event.chat_id, from_user=owner):
        await msg.delete()
@ok
@ABH.on(events.NewMessage(pattern=r'^.كلمة (.+)$'))
async def word(event):
    input_value = event.pattern_match.group(1)
    try:
        word = int(input_value)
    except ValueError:
        word = input_value
    await event.delete()
    async for msg in ABH.iter_messages(event.chat_id):
        if msg.text:
             if isinstance(word, str):
                if word.lower() in msg.text.lower():
                    await msg.delete()
                elif isinstance(word, int):
                    if str(word) in msg.text:
                        await msg.delete()
async def main():
    await ABH.start()
    await ABH.run_until_disconnected()
print("usbot is running ◉")
th
asyncio.run(main())
