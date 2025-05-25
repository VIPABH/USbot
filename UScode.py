from shortcuts import shortcuts #type: ignore
from ABH import ABH, ok, events #type:ignore
from zoneinfo import ZoneInfo  
import asyncio, unicodedata
@ABH.on(events.NewMessage(pattern=r'^.تثبيت$', outgoing=True))
async def pin(event):
    s = shortcuts(event)
    await event.delete()
    gid = event.chat_id
    r = await event.get_reply_message()
    await ABH.pin_message(gid, r.id)
@ABH.on(events.NewMessage(pattern=r'^.الغاء تثبيت$', outgoing=True))
async def unpin(event):
    await event.delete()
    gid = event.chat_id
    r = await event.get_reply_message()
    await ABH.unpin_message(gid, r.id)
@ABH.on(events.NewMessage(pattern=r'^.الايدي$', outgoing=True))
async def id(event):
    r = await event.get_reply_message()
    gid = event.chat_id if not event.is_private else None
    if r:
        uid = r.sender_id
        await event.edit(f"ايدي المستخدم: `{uid}`\nايدي المجموعة: `{gid}`")
    else:
        chat = await event.get_chat()
        await event.edit(f"ايدي المجموعة: `{chat.id}`")
@ABH.on(events.NewMessage(pattern=r'^.خاص$', outgoing=True))
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
@ABH.on(events.NewMessage(pattern=r'^.مسح(?: (\d+))?$', outgoing=True))
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
@ABH.on(events.NewMessage(pattern=r'^؟؟$', outgoing=True))
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
@ABH.on(events.NewMessage(pattern=r'^رسالة (\S+) (.+)$', outgoing=True))
async def send(event):
    r = await event.get_reply_message()
    if r:
         await event.delete()
         to = r.sender_id
         t1 = event.pattern_match.group(1)
         txt = event.pattern_match.group(2)
         text = f"{t1} {txt}"
         entity = await ABH.get_input_entity(to)
         await ABH.send_message(entity, text)
    else:
        await event.delete()
        to = event.pattern_match.group(1)
        text = event.pattern_match.group(2)
        entity = await ABH.get_input_entity(to)
        await ABH.send_message(entity, text)
@ABH.on(events.NewMessage(pattern=r'^وقتي (\d+)\s+(.+)$', outgoing=True))
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
@ABH.on(events.NewMessage(pattern=r'^.مسح رسائلي$', outgoing=True))
async def dele_me(event):
     owner = (await ABH.get_me()).id
     await event.delete()
     async for msg in ABH.iter_messages(event.chat_id, from_user=owner):
         await msg.delete()
@ABH.on(events.NewMessage(pattern=r'^.حذف مشاركاته$', outgoing=True))
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
@ABH.on(events.NewMessage(pattern=r".وسبام (.+)", outgoing=True))
async def tmeme(event):
    text = event.pattern_match.group(1)
    words = text.split()
    await event.delete()
    for word in words:
        await event.respond(word)
def normalize_text(text):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text)
        if not unicodedata.combining(c)
    ).lower().strip()
@ABH.on(events.NewMessage(pattern=r'^.كلمة (.+)$', outgoing=True))
async def word(event):
    keyword_raw = event.pattern_match.group(1)
    keyword = normalize_text(keyword_raw)
    async for msg in ABH.iter_messages(event.chat_id):
        if msg.text:
            msg_normalized = normalize_text(msg.text)
            if keyword in msg_normalized:
                await msg.delete()
@ABH.on(events.NewMessage(pattern=r"^مكرر\s+(\d+)\s+(\d+(?:\.\d+)?)$", outgoing=True))
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
@ABH.on(events.NewMessage(pattern=r'^.كرر(?: (\d+))?$', outgoing=True))
async def repeat_it(event):
    num = int(event.pattern_match.group(1) or 1)
    r = await event.get_reply_message()
    if r:
        for i in range(num):
            await event.delete()
            await event.respond(r)
x = False
t = 3 
@ABH.on(events.NewMessage(pattern=r'الحذف تفعيل$', outgoing=True))
async def delete_on(event):
    global x
    if x:
        await event.edit('الحذف التلقائي مفعل بالفعل')
        await asyncio.sleep(3)
        await event.delete()
    else:
        await event.edit('تم تفعيل الحذف التلقائي')
        x = True
@ABH.on(events.NewMessage(pattern=r'الحذف تعطيل$', outgoing=True))
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
@ABH.on(events.NewMessage(outgoing=True))
async def delete_auto(event):
    global x
    if x:
        await asyncio.sleep(t)
        await event.delete()
@ABH.on(events.NewMessage(pattern=r'^الحذف (\d+)$', outgoing=True))
async def set(event):
    global t
    t = int(event.pattern_match.group(1))
    await event.edit(f'تم تعيين وقت الحذف التلقائي إلى {t} ثواني')
    await asyncio.sleep(3)
    await event.delete()
@ABH.on(events.NewMessage(pattern=r'^متى$', outgoing=True))
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
@ABH.on(events.NewMessage(pattern=r'^.تقييد|ت$', outgoing=True))
async def mute(event):
    r = await event.get_reply_message()
    if not r:
        await event.edit('🤔 يجب أن ترد على رسالة.')
        await asyncio.sleep(3)
        await event.delete()
        return
    else:
        gid = event.chat_id
        uid = r.sender_id
        await ABH.edit_permissions(gid, uid, send_messages=False)
        await event.edit('الئ رحمة الله')
        await r.delete()
        await asyncio.sleep(3)
        await event.delete()
x = []
@ABH.on(events.NewMessage(pattern=r'^.كتم$', outgoing=True))
async def muteINall(event):
    c = await event.get_chat()
    if c.is_channel:
        return
    r = await event.get_reply_message()
    if not r:
        await event.edit('🤔 يجب أن ترد على رسالة.')
        await asyncio.sleep(3)
        await event.delete()
        return
    else:
        x[c.id] = {'uid': r.sender_id}
@ABH.on(events.NewMessage(pattern=r'^.الغاء كتم$', outgoing=True))
async def unmute(event):
    c = await event.get_chat()
    if c.is_channel:
        return
    r = await event.get_reply_message()
    if not r:
        await event.edit('🤔 يجب أن ترد على رسالة.')
        await asyncio.sleep(3)
        await event.delete()
        return
    else:
        if c.id in x and x[c.id]['uid'] == r.sender_id:
            del x[c.id]
            await event.edit('تم الغاء كتمه')
            await asyncio.sleep(3)
            await event.delete()
        else:
            await event.edit('هذا المستخدم ليس مكتومًا')
            await asyncio.sleep(3)
            await event.delete()
@ABH.on(events.NewMessage)
async def check_mute(event):
    c = await event.get_chat()
    if c.is_channel:
        return
    if c.id in x and x[c.id]['uid'] == event.sender_id:
        await event.delete()
        return
    if x and c.id not in x:
        return
    if not x:
        return
    if event.is_private:
        return
    if not event.text:
        return
    # if event.sender_id in (await ABH.get_blocked_users()):
    #     return
