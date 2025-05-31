from telethon.tl.types import Message
from telethon import events
from ABH import ABH
import os, re
ABH_Asbo3={'Monday':'الاثنين','Tuesday':'الثلاثاء','Wednesday':'الأربعاء','Thursday':'الخميس','Friday':'الجمعة','Saturday':'السبت','Sunday':'الأحد'}
@ABH.on(events.NewMessage(pattern=r"^جلب(?: (.+))?$", outgoing=True))
async def g(event):
    input_link = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if reply and reply.media:
        await event.edit(" يتم حفظ الوسائط من الرد...")
        await Hussein_event(reply)
        return
    elif input_link:
        match = re.match(r"https://t\.me/c/(\d+)/(\d+)", input_link)
    if match:
        chat_id = int("-100" + match.group(1))
        msg_id = int(match.group(2))
        msg = await ABH.get_messages(chat_id, ids=msg_id)
        if isinstance(msg, Message) and msg.media:
            await Hussein_event(msg)
            return
async def Hussein(event, input_link):
    me = await ABH.get_me()
    x = me.id
    caption = "- تـم حفظ الوسائط من الرسالة ✓"
    media = await ABH.download_media(input_link)
    if not media:
        await event.edit("لم يتم تحميل الوسائط من الرابط.")
        return
    await ABH.send_file(x, media, caption=caption)
    if os.path.exists(media):
        os.remove(media)
async def Hussein_event(message, caption):
    media = await message.download_media()
    if not media:
        await message.reply(" لم يتم تحميل الوسائط من الرسالة.")
        return
    x = await ABH.get_me()
    x = x.id
    await ABH.send_file(x, media, caption=caption, parse_mode="markdown")
    if os.path.exists(media):
        os.remove(media)
def joker_unread_media(message):
    return message.media_unread and (message.photo or message.video)
async def Hussein_event(event, caption):
    media = await event.download_media()
    if not media:
        await event.edit(" لم يتم تحميل الوسائط.")
        return
    await ABH.send_file("me", media, caption=caption, parse_mode="markdown")    
    if os.path.exists(media):
        os.remove(media)
@ABH.on(events.NewMessage(func=lambda e:e.is_private and joker_unread_media(e)))
async def Reda(event):
 a=event.sender.first_name
 b=event.sender_id
 c=event.date.strftime("%Y-%m-%d")
 d=ABH_Asbo3[event.date.strftime("%A")]
 caption=f"""**
♡ تم حفظ الذاتية بنجاح ✓
♡ أسم المرسل : [{a}](tg://user?id={b})
♡  تاريخ الذاتية : `{c}`
♡  أرسلت في يوم `{d}`
♡    ABH    ♡
**"""
 await Hussein_event(event,caption)
