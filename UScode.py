from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji, ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
import asyncio, unicodedata, time, json, os
from ABH import ABH #type:ignore
from datetime import datetime
from zoneinfo import ZoneInfo  
from telethon import events
@ABH.on(events.NewMessage(pattern=r'^.تثبيت$', outgoing=True))
async def pin(event):
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
@ABH.on(events.NewMessage(pattern=r'^خاص|.خاص$', outgoing=True))
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
@ABH.on(events.NewMessage(pattern=r'^\.مسح(?: (\d{1,3}))?$', outgoing=True))
async def delet(event):
    num = event.pattern_match.group(1) or 0
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
        msg2 = await event.edit(f'{m}')
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
        await event.edit(f'{word}')
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
@ABH.on(events.NewMessage(pattern=r'^\.?مكرر\s+(\d+)\s+(\d+(?:\.\d+)?)$', outgoing=True))
async def repeat(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        m = await event.respond('🤔 يجب أن ترد على رسالة.')
        await asyncio.sleep(3)
        await m.delete()
        return
    else:
        count = int(event.pattern_match.group(1))
        delay = float(event.pattern_match.group(2))
        for _ in range(count):
            await asyncio.sleep(delay)
            await event.respond(
                message=r.message if r.message else None,
                file=r.media if r.media else None
            )
@ABH.on(events.NewMessage(pattern=r'^.كرر|كرر(?: (\d+))?$', outgoing=True))
async def repeat_it(event):
    num = int(event.pattern_match.group(1) or 1)
    r = await event.get_reply_message()
    if r:
        await event.delete()
        for _ in range(num):
            await event.respond(
                message=r.message if r.message else None,
                file=r.media if r.media else None
            )
الحذف = False
t = 3 
@ABH.on(events.NewMessage(pattern=r'الحذف تفعيل$', outgoing=True))
async def delete_on(event):
    global الحذف
    if الحذف:
        await event.edit('الحذف التلقائي مفعل بالفعل')
        await asyncio.sleep(3)
        await event.delete()
    else:
        await event.edit('تم تفعيل الحذف التلقائي')
        الحذف = True
@ABH.on(events.NewMessage(pattern=r'الحذف تعطيل$', outgoing=True))
async def delete_off(event):
    global الحذف
    if not الحذف:
        await event.edit('الحذف التلقائي معطل بالفعل')
        await asyncio.sleep(3)
        await event.delete()
    else:
        await event.edit('تم تعطيل الحذف التلقائي')
        الحذف = False
        await asyncio.sleep(3)
        await event.delete()
@ABH.on(events.NewMessage(outgoing=True))
async def delete_auto(event):
    global الحذف
    if الحذف:
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
        await event.edit('الئ رحمة الله')
        await ABH.edit_permissions(gid, uid, send_messages=False)
        await r.delete()
        await asyncio.sleep(3)
        await event.delete()
المكتومين = {}
@ABH.on(events.NewMessage(pattern=r'^.كتم$', outgoing=True))
async def muteINall(event):
    c = await event.get_chat()
    r = await event.get_reply_message()
    if not r:
        await event.edit('🤔 يجب أن ترد على رسالة.')
        await asyncio.sleep(3)
        await event.delete()
        return
    المكتومين[c.id] = {'uid': r.sender_id}
    await event.edit("قل اهلا لقائمة المكتومين")
    await asyncio.sleep(3)
    await event.delete()
@ABH.on(events.NewMessage(pattern=r'^.الغاء كتم$', outgoing=True))
async def unmute(event):
    c = await event.get_chat()
    r = await event.get_reply_message()
    if not r:
        await event.edit('🤔 يجب أن ترد على رسالة.')
        await asyncio.sleep(3)
        await event.delete()
        return
    if c.id in المكتومين and المكتومين[c.id]['uid'] == r.sender_id:
        del المكتومين[c.id]
        await event.edit('تم الغاء كتم المستخدم')
    else:
        await event.edit('هذا المستخدم ليس مكتومًا')
    await asyncio.sleep(3)
    await event.delete()
@ABH.on(events.NewMessage)
async def check_mute(event):
    c = await event.get_chat()
    if c.id in المكتومين and المكتومين[c.id]['uid'] == event.sender_id:
        await event.delete()
ازعاج = {}
@ABH.on(events.NewMessage(pattern=r'^\.ازعاج(?: (.+))?$', outgoing=True))
async def muteINall(event):
    global ازعاج, p
    p = event.pattern_match.group(1) or '👍'
    c = await event.get_chat()
    r = await event.get_reply_message()
    if not r:
        await event.edit('🤔 يجب أن ترد على رسالة.')
        await asyncio.sleep(3)
        await event.delete()
        return
    ازعاج[c.id] = {'uid': r.sender_id}
    await event.edit("قل اهلا لقائمة الازعاج")
    await asyncio.sleep(3)
    await event.delete()
@ABH.on(events.NewMessage(pattern=r'^.الغاء ازعاج$', outgoing=True))
async def unmute(event):
    c = await event.get_chat()
    r = await event.get_reply_message()
    if not r:
        await event.edit('🤔 يجب أن ترد على رسالة.')
        await asyncio.sleep(3)
        await event.delete()
        return
    if c.id in ازعاج and ازعاج[c.id]['uid'] == r.sender_id:
        del ازعاج[c.id]
        await event.edit('تم الغاء الازعاج')
    else:
        await event.edit('هذا المستخدم لا يوجد عليه ازعاج')
    await asyncio.sleep(3)
    await event.delete()
@ABH.on(events.NewMessage)
async def check_mute(event):
    c = await event.get_chat()
    if c.id in ازعاج and ازعاج[c.id]['uid'] == event.sender_id:
        await ABH(SendReactionRequest(
            peer=event.chat_id,
            msg_id=event.id,
            reaction=[ReactionEmoji(emoticon=p)]
    ))
user_ban_data = {}
rights = ChatBannedRights(
    until_date=None,
    send_messages=True)
@ABH.on(events.NewMessage(pattern='^(حظر|.حظر|حظر$|/حظر)(.*)'))
async def anti_spam_ban(event):
    user_id = event.sender_id
    now = time.time()
    chat = await event.get_chat()
    if user_id not in user_ban_data:
        user_ban_data[user_id] = {"count": 0, "first_time": now}
    data = user_ban_data[user_id]
    if now - data["first_time"] > 3:
        data["count"] = 0
        data["first_time"] = now
    data["count"] += 1
    if data["count"] >= 5:
            await ABH(EditBannedRequest(channel=chat.id, participant=user_id, banned_rights=rights))
            user_ban_data[user_id] = {"count": 0, "first_time": now}
@ABH.on(events.NewMessage(pattern=r'^جدوله\s+(\d{1,2})/(\d{1,2})/(\d{1,2})/(\d{1,2})$', outgoing=True))
async def schedule_handler(event):
    if not event.is_reply:
        await event.edit(" يجب الرد على الرسالة التي تريد جدولتها.")
        return
    month = int(event.pattern_match.group(1))
    day = int(event.pattern_match.group(2))
    hour = int(event.pattern_match.group(3))
    minute = int(event.pattern_match.group(4))
    now = datetime.now()
    scheduled_time = datetime(
        year=now.year,
        month=month,
        day=day,
        hour=hour,
        minute=minute,
        second=0,
        microsecond=0
    )
    if scheduled_time <= now:
        await event.edit("الوقت الذي أدخلته قد مضى. الرجاء إدخال وقت مستقبلي.")
        return
    reply = await event.get_reply_message()
    file = reply.media if reply.media else None
    msg = reply.message if reply.message else None
    if not msg and not file:
        await event.edit("لا يمكن جدولة هذه الرسالة (قد تكون نوع غير مدعوم).")
        return
    await ABH.send_message(
        entity=event.chat_id,
        message=msg or "",
        file=file,
        schedule=scheduled_time
    )
    await event.edit(
        f" تم جدولة الرسالة بتاريخ {month:02}/{day:02} الساعة {hour:02}:{minute:02}."
    )
USAGE_FILE = "usage.json"
def load_usage():
    if not os.path.exists(USAGE_FILE):
        return {"on": False, "usage": 0, "limit": 2, "last_reset": datetime.now().strftime("%Y-%m-%d")}
    with open(USAGE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
def save_usage(data):
    with open(USAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
@ABH.on(events.NewMessage(pattern=r'^الحد اليومي (.+)$', outgoing=True))
async def on_off(event):
    data = load_usage()
    command = event.pattern_match.group(1)
    if command == 'تفعيل':
        data['on'] = True
        await event.edit(" تم تفعيل النظام اليومي.")
    elif command == 'تعطيل':
        data['on'] = False
        await event.edit(" تم تعطيل النظام اليومي.")
    save_usage(data)
@ABH.on(events.NewMessage(pattern=r'\.?استخدامي', outgoing=True))
async def show_usage(event):
    data = load_usage()
    await event.edit(f"عدد رسائلك {data['usage']}")
@ABH.on(events.NewMessage(pattern=r'^ضع حد يومي (\d+)$', outgoing=True))
async def set_daily_limit(event):
    data = load_usage()
    data['limit'] = int(event.pattern_match.group(1))
    save_usage(data)
    await event.edit(f"تم تعيين الحد اليومي إلى {data['limit']} استخدام.")
@ABH.on(events.NewMessage(outgoing=True))
async def count_usage(event):
    if event.raw_text.startswith(('.', 'الحد اليومي', 'ضع حد يومي')):
        return
    data = load_usage()
    if data['usage'] >= data['limit']:
        await event.delete()
    data = load_usage()
    today = datetime.now().strftime("%Y-%m-%d")
    if data.get("last_reset") != today:
        data["usage"] = 0
        data["last_reset"] = today
    if data['on']:
        data['usage'] += 1
    save_usage(data)
