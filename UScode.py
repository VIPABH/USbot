from ABH import ABH, ok, events #type:ignore
from zoneinfo import ZoneInfo  
import asyncio
@ok
@ABH.on(events.NewMessage(pattern=r'^.تثبيت$'))
async def pin(event):
    await event.delete()
    gid = event.chat_id
    r = await event.get_reply_message()
    await ABH.pin_message(gid, r.id)
@ok
@ABH.on(events.NewMessage(pattern=r'^الغاء تثبيت$'))
async def unpin(event):
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
    if not r:
        await event.edit('🤔 يجب أن ترد على رسالة.')
        await asyncio.sleep(3)
        await event.delete()
        return
    else:
        await event.delete()
        await r.forward_to(me.id)
@ok
@ABH.on(events.NewMessage(pattern=r'^.مسح(?: (\d+))?$'))
async def delet(event):
    num = event.pattern_match.group(1)
    r = await event.get_reply_message()
    if r:
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
async def dele_me(event):
     owner = (await ABH.get_me()).id
     await event.delete()
     async for msg in ABH.iter_messages(event.chat_id, from_user=owner):
         await msg.delete()
@ok
@ABH.on(events.NewMessage(pattern=r'^.حذف مشاركاته$'))
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
@ABH.on(events.NewMessage(pattern=r".وسبام (.+)"))
async def tmeme(event):
    text = event.pattern_match.group(1)
    words = text.split()
    await event.delete()
    for word in words:
        await event.respond(word)
@ok
@ABH.on(events.NewMessage(pattern=r'^.كلمة (.+)$'))
async def word(event):
     input_value = event.pattern_match.group(1)
     word = int(input_value)
     async for msg in ABH.iter_messages(event.chat_id):
        if msg.text:
            if isinstance(word, str):
                if word.lower() in msg.text.lower():
                    await msg.delete()
                elif isinstance(word, int):
                    if str(word) in msg.text:
                        await msg.delete()
@ok
@ABH.on(events.NewMessage(pattern=r"^مكرر\s+(\d+)\s+(\d+(?:\.\d+)?)$"))
async def repeat(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        await event.edit('🤔 يجب أن ترد على رسالة.')
        await asyncio.sleep(3)
        await event.delete()
        return
    else:
        much = int(event.pattern_match.group(1))
        time = float(event.pattern_match.group(2))
        for i in range(int(much)):
            await asyncio.sleep(float(time))
            await event.respond(r.text)
@ok
@ABH.on(events.NewMessage(pattern=r'^.كرر(?: (\d+))?$'))
async def repeat_it(event):
    num = event.pattern_match.group(1)
    r = await event.get_reply_message()
    if r:
        for i in range(int(num)):
            await event.delete()
            await event.respond(r)
x = False
t = 3 
@ok
@ABH.on(events.NewMessage(pattern=r'الحذف تفعيل$'))
async def delete_on(event):
    global x
    if x:
        await event.edit('الحذف التلقائي مفعل بالفعل')
        await asyncio.sleep(3)
        await event.delete()
    else:
        await event.edit('تم تفعيل الحذف التلقائي')
        x = True
@ok
@ABH.on(events.NewMessage(pattern=r'الحذف تعطيل$'))
async def delete_off(event):
    global x
    if not x:
        await event.edit('الحذف التلقائي معطل بالفعل')
        await asyncio.sleep(3)
        await event.delete()
    else:
        await event.edit('تم تعطيل الحذف التلقائي')
        x = False
        await asyncio.sleep(3)
        await event.delete()
@ok
@ABH.on(events.NewMessage(outgoing=True))
async def delete_auto(event):
    global x
    if x:
        await asyncio.sleep(t)
        await event.delete()
@ok
@ABH.on(events.NewMessage(pattern=r'^الحذف (\d+)$'))
async def set(event):
    global t
    t = int(event.pattern_match.group(1))
    await event.edit(f'تم تعيين وقت الحذف التلقائي إلى {t} ثواني')
    await asyncio.sleep(3)
    await event.delete()
@ok 
@ABH.on(events.NewMessage(pattern=r'^متى$'))
async def when(event):
    r = await event.get_reply_message()
    if not r:
        m = event.message
        message_time = m.date.astimezone(ZoneInfo("Asia/Baghdad"))
        formatted_time = message_time.strftime('%Y/%m/%d %I:%M:%S %p')
        await event.edit(formatted_time)
    else:
        message_time = r.date.astimezone(ZoneInfo("Asia/Baghdad"))
        formatted_time = message_time.strftime('%Y/%m/%d %I:%M:%S %p')
        await event.edit(formatted_time)
print('UScode is running')
