from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.types import ReactionEmoji, ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.photos import DeletePhotosRequest
from telethon.errors import PhotoCropSizeSmallError
import asyncio, unicodedata, re, time, json, os
from telethon.tl.types import InputPhoto
from telethon import events, functions
from ABH import ABH #type:ignore
from datetime import datetime
from zoneinfo import ZoneInfo  
wfffp = 1910015590
@ABH.on(events.NewMessage(pattern=r'^.تثبيت$', outgoing=True))
async def pin(event):
    await event.delete()
    gid = event.chat_id
    r = await event.get_reply_message()
    await ABH.pin_message(gid, r.id)
@ABH.on(events.NewMessage(pattern=r'^.?الغاء تثبيت$', outgoing=True))
async def unpin(event):
    await event.delete()
    gid = event.chat_id
    r = await event.get_reply_message()
    await ABH.unpin_message(gid, r.id)
@ABH.on(events.NewMessage(pattern=r'^.?الايدي$', outgoing=True))
async def id(event):
    r = await event.get_reply_message()
    chat = await event.get_chat()
    if r:
        uid = r.sender_id
        await event.edit(f'ايدي المجموعة ↢ `{chat.id}` \n ايدي المستخدم ↢ `{uid}`')
    else:
        await event.edit(f"ايدي المجموعة: `{chat.id}`")
@ABH.on(events.NewMessage(pattern=r'^.?خاص$', outgoing=True))
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
        await event.edit("`\\`")
        await asyncio.sleep(0.4)
@ABH.on(events.NewMessage(pattern=r'^\.?رسالة(?: (\S+))? (.+)$', outgoing=True))
async def send(event):
    await event.delete()
    reply = await event.get_reply_message()
    arg1 = event.pattern_match.group(1)
    message_text = event.pattern_match.group(2)
    if reply:
        to_id = reply.sender_id
        entity = await ABH.get_input_entity(to_id)
        await ABH.send_message(entity, f"{arg1} {message_text}")
    elif arg1 and (arg1.startswith("@") or arg1.isdigit()):
        entity = await ABH.get_input_entity(arg1)
        await ABH.send_message(entity, message_text)
    else:
        await event.edit(f"📩 نص الرسالة:\n`{arg1} {message_text}`\n لم يتم تحديد جهة لإرسال الرسالة.")
@ABH.on(events.NewMessage(pattern=r'^.?وقتي (\d+)\s+(.+)$', outgoing=True))
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
@ABH.on(events.NewMessage(pattern=r".?وسبام (.+)", outgoing=True))
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
def normalize_text(text):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text)
        if not unicodedata.combining(c)
    ).lower().strip()
@ABH.on(events.NewMessage(pattern=r'^.كلمة (.+)$', outgoing=True))
async def word(event):
    keyword_raw = event.pattern_match.group(1)
    keyword = normalize_text(keyword_raw)
    pattern = re.compile(rf'\b{re.escape(keyword)}\b')
    async for msg in ABH.iter_messages(event.chat_id):
        if msg.text:
            msg_normalized = normalize_text(msg.text)
            if pattern.search(msg_normalized):
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
@ABH.on(events.NewMessage(pattern=r'^\.?كرر(?: (\d+))?$', outgoing=True))
async def repeat_it(event):
    await event.delete()
    num = int(event.pattern_match.group(1) or 1)
    r = await event.get_reply_message()
    if not r:
        m = await event.respond('🤔 يجب أن ترد على رسالة.')
        await asyncio.sleep(3)
        await m.delete()
        return
    else:
        for _ in range(num):
            await event.respond(
                message=r.message if r.message else None,
                file=r.media if r.media else None
            )
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
async def muteI(event):
    global ازعاج, p
    p = event.pattern_match.group(1) or '👍'
    c = await event.get_chat()
    r = await event.get_reply_message()
    if not r:
        await event.edit('🤔 يجب أن ترد على رسالة.')
        await asyncio.sleep(3)
        await event.delete()
        return
    if r.sender_id == wfffp:
        await event.edit('هههههههه لتعيدها المطور هاذ')
        await asyncio.sleep(3)
        await event.delete()
        return
    ازعاج[c.id] = {'uid': r.sender_id}
    await event.edit("قل اهلا لقائمة الازعاج")
    await asyncio.sleep(3)
    await event.delete()
@ABH.on(events.NewMessage(pattern=r'^.الغاء ازعاج$', outgoing=True))
async def unmu(event):
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
@ABH.on(events.NewMessage(pattern=r'^جدوله\s+(\d{1,2})/(\d{1,2})/(\d{1,2})$', outgoing=True))
async def schedule_handler(event):
    if not event.is_reply:
        await event.edit("❌ يجب الرد على الرسالة التي تريد جدولتها.")
        return
    try:
        day = int(event.pattern_match.group(1))
        hour = int(event.pattern_match.group(2))
        minute = int(event.pattern_match.group(3))
    except ValueError:
        await event.edit("❌ صيغة غير صحيحة للأرقام المدخلة.")
        return
    now = datetime.now()
    month = now.month
    year = now.year
    try:
        scheduled_time = datetime(
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            second=0,
            microsecond=0
        )
    except ValueError:
        await event.edit("❌ التاريخ أو الوقت المدخل غير صحيح.")
        return
    if scheduled_time <= now:
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

        try:
            scheduled_time = datetime(
                year=year,
                month=month,
                day=day,
                hour=hour,
                minute=minute,
                second=0,
                microsecond=0
            )
        except ValueError:
            await event.edit("❌ التاريخ أو الوقت المدخل غير صحيح بعد تعديل الشهر.")
            return
    reply = await event.get_reply_message()
    if not reply:
        await event.edit("❌ يرجى الرد على الرسالة التي تريد جدولتها.")
        return
    file = reply.media if reply.media else None
    msg = reply.message if reply.message else ""
    if not msg and not file:
        await event.edit("❌ لا يمكن جدولة هذه الرسالة (نوع غير مدعوم).")
        return
    await ABH.send_message(
        entity=event.chat_id,
        message=msg,
        file=file,
        schedule=scheduled_time
    )
    await event.edit(
        f"✅ تم جدولة الرسالة بتاريخ {scheduled_time.strftime('%d/%m/%Y %H:%M')}."
    )
@ABH.on(events.NewMessage(pattern=r'^تغيير صورتي$', outgoing=True))
async def change_photo(e):
    if not e.is_reply:
        await e.edit("❗️يجب أن ترد على صورة لتعيينها كصورة شخصية.")
        return
    reply = await e.get_reply_message()
    if not reply.photo:
        await e.edit("❗️الرد يجب أن يكون على صورة.")
        return
    await e.edit("📤 جاري تحميل وتغيير الصورة الشخصية...")
    temp_path = "temp_profile_photo.jpg"
    try:
        photo_path = await reply.download_media(file=temp_path)
        if not os.path.exists(photo_path):
            await e.edit("❌ فشل تحميل الصورة.")
            return
        input_file = await ABH.upload_file(photo_path)
        await ABH(UploadProfilePhotoRequest(file=input_file))
        await e.edit("✅ تم تغيير الصورة الشخصية بنجاح.")
        await asyncio.sleep(3)
        await e.delete()
    except PhotoCropSizeSmallError:
        await e.edit("❌ الصورة صغيرة جدًا. اختر صورة أكبر.")
    except Exception as ex:
        await e.edit(f"❌ حدث خطأ أثناء تغيير الصورة:\n`{ex}`")
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
@ABH.on(events.NewMessage(pattern=r'^تغيير اسمي (.+)$', outgoing=True))
async def change_name(e):
    new_name = e.pattern_match.group(1).strip()
    if not new_name:
        await e.edit('❗️يرجى إدخال اسم صحيح.')
        return
    try:
        await ABH(UpdateProfileRequest(first_name=new_name))
        await e.edit(f'✅ تم تغيير اسم الحساب إلى: {new_name}')
        await asyncio.sleep(3)
        await e.delete()
    except Exception as ex:
        await e.edit(f"❌ حدث خطأ أثناء تغيير الاسم:\n`{ex}`")
@ABH.on(events.NewMessage(pattern=r'^حذف صورتي$', outgoing=True))
async def delete_last_photo(e):
    await e.edit("📤 جاري حذف آخر صورة شخصية...")
    try:
        photos = await ABH.get_profile_photos('me', limit=1)
        if not photos:
            await e.edit("❗️لا توجد صورة شخصية لحذفها حالياً.")
            return
        await ABH(DeletePhotosRequest(id=[
            InputPhoto(
                id=photos[0].id,
                access_hash=photos[0].access_hash,
                file_reference=photos[0].file_reference
            )
        ]))
        await e.edit("✅ تم حذف آخر صورة شخصية بنجاح.")
        await asyncio.sleep(3)
        await e.delete()
    except Exception as ex:
        await e.edit(f"❌ حدث خطأ أثناء حذف الصورة:\n`{ex}`")
@ABH.on(events.NewMessage(pattern=r'^منصب؟$', from_users=1910015590))
async def check_admin(event):
    me = await ABH.get_me()
    id = me.id
    if id == 1910015590:
        return
    r = await event.get_reply_message()
    if not r:
        return
    if r.id == wfffp:
        return
    await event.reply("نعم، أنا منصب هنا.")
@ABH.on(events.NewMessage(pattern=r'^منو تاج راسك؟$', from_users=1910015590))
async def asc(event):
    me = await ABH.get_me()
    id = me.id
    if id == 1910015590:
        return
    r = await event.get_reply_message()
    if not r:
        return
    if r.id == wfffp:
        return
    await event.reply("الامام علي.")
@ABH.on(events.NewMessage(pattern='^بلوك$', outgoing=True))
async def block(event):
    if event.is_private:
        user_id = event.chat_id
    elif event.is_group and event.is_reply:
        r = await event.get_reply_message()
        user_id = r.sender_id
    await ABH(functions.contacts.BlockRequest(user_id))
    await event.edit(f" تم حظر المستخدم ")
    await asyncio.sleep(3)
    await event.delete()
@ABH.on(events.NewMessage(pattern='^الغاء بلوك$', outgoing=True))
async def unblock(event):
    if event.is_private:
        user_id = event.chat_id
    elif event.is_group and event.is_reply:
        r = await event.get_reply_message()
        user_id = r.sender_id
    await ABH(functions.contacts.UnblockRequest(user_id))
    await event.edit(" تم إلغاء الحظر عن المستخدم")
    await asyncio.sleep(3)
    await event.delete()
@ABH.on(events.NewMessage(pattern=r"عداد (\d+)", outgoing=True))
async def countdown(event):
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("لازم تعين رقم بعد الامر")
        await asyncio.sleep(3)
        await event.delete()
        return
    try:
        num = int(text)
    except ValueError:
        await event.edit("الرقم غير صالح!")
        await asyncio.sleep(3)
        await event.delete()
        return
    for i in range(num, 0, -1):
        await event.edit(str(i))
        await asyncio.sleep(1)
    await e.edit(f"انتهى العد التنازلي من {num}")
