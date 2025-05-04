from ABH import ABH, ok, events #type:ignore
import asyncio
@ok
@ABH.on(events.NewMessage(pattern=r'^.تثبيت$'))
async def pin(event):
    uid = event.sender_id
    me = await ABH.get_me()
    uid == me.id
    if uid == me.id:
        await event.delete()
        gid = event.chat_id
        r = await event.get_reply_message()
        await ABH.pin_message(gid, r.id)
@ok
@ABH.on(events.NewMessage(pattern=r'^الغاء تثبيت$'))
async def pin(event):
    uid = event.sender_id
    me = await ABH.get_me()
    uid == me.id
    if uid == me.id:
        await event.delete()
        gid = event.chat_id
        r = await event.get_reply_message()
        await ABH.unpin_message(gid, r.id)
@ok
@ABH.on(events.NewMessage(pattern=r'^.خاص$'))
async def save(event):
    uid = event.sender_id
    me = await ABH.get_me()
    r = await event.get_reply_message()
    uid = event.sender_id
    me = await ABH.get_me()
    uid == me.id    
    if not r and uid == me.id:
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
    num = event.pattern_match.group(1)
    r = await event.get_reply_message()
    uid = event.sender_id
    me = await ABH.get_me()
    uid == me.id    
    if r and uid == me.id:
        await event.delete()
        await r.delete()
    else:
         messages = []
         async for msg in ABH.iter_messages(event.chat_id, limit=int(num) + 1):
              messages.append(msg.id)
              await ABH.delete_messages(event.chat_id, messages)
@ok
@ABH.on(events.NewMessage(pattern=r'^؟؟$'))
async def edit(event):
    uid = event.sender_id
    me = await ABH.get_me()
    uid == me.id
    if uid == me.id:
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
    uid = event.sender_id
    me = await ABH.get_me()
    uid == me.id
    r = await event.get_reply_message()
    if r and uid == me.id:
         await event.delete()
         to = r.sender_id
         t1 = event.pattern_match(1)
         txt = event.pattern_match(2)
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
    uid = event.sender_id
    me = await ABH.get_me()
    if r and uid == me.id:
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
    uid = event.sender_id
    me = await ABH.get_me()
    if uid == me.id:
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
    uid = event.sender_id
    me = await ABH.get_me()
    r = await event.get_reply_message()
    if not r and uid == me.id:
        await event.edit('🤔 يجب أن ترد على رسالة.')
        await asyncio.sleep(3)
        await event.delete()
        return
    owner = r.sender_id
    await event.delete()
    async for msg in ABH.iter_messages(event.chat_id, from_user=owner):
        await msg.delete()
@ok
@ABH.on(events.NewMessage(pattern=r".وسبام (.+)"))
async def tmeme(event):
    uid = event.sender_id
    me = await ABH.get_me()
    if uid == me.id:
        text = event.pattern_match.group(1)
        words = text.split()
        await event.delete()
        for word in words:
            await event.respond(word)
@ok
@ABH.on(events.NewMessage(pattern=r'^.كلمة (.+)$'))
async def word(event):
    uid = event.sender_id
    me = await ABH.get_me()
    if uid == me.id:
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
print('UScode is running')
