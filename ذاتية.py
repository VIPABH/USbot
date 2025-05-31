from telethon import events
from ABH import ABH
import os
ABH_Asbo3={'Monday':'الاثنين','Tuesday':'الثلاثاء','Wednesday':'الأربعاء','Thursday':'الخميس','Friday':'الجمعة','Saturday':'السبت','Sunday':'الأحد'}
@ABH.on(events.NewMessage(pattern=r"^جلب (.+)$", outgoing=True))
async def g(event):
    input_link = event.pattern_match.group(1)
    await event.edit(f" يتم الحفظ: {input_link}")
    caption = "- تـم حفظ الصـورة بنجـاح ✓"
    try:
        await Hussein(event, caption, input_link)
    except Exception as e:
        await event.edit(f"❌ خطأ أثناء الحفظ:\n{e}")
async def Hussein(event, caption, input_link):
    me = await ABH.get_me()
    x = me.id
    media = await ABH.download_media(input_link)
    if not media:
        await event.edit(" لم يتم تحميل الوسائط.")
        return
    await ABH.send_file(x, media, caption=caption)
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
