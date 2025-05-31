from ABH import *
import os,asyncio
from telethon import events
ABH_Asbo3={'Monday':'الاثنين','Tuesday':'الثلاثاء','Wednesday':'الأربعاء','Thursday':'الخميس','Friday':'الجمعة','Saturday':'السبت','Sunday':'الأحد'}
@ABH.on(events.NewMessage(pattern=r"^جلب (.+)$", outgoing=True))
async def g(event):
 input_link=event.pattern_match.group(1)
 await event.edit(f"يتم الحفظ {input_link}")
 caption="- تـم حفظ الصـورة بنجـاح ✓"
 await Hussein(event,caption,input_link)
 await event.delete()
async def Hussein(event,caption,input_link):
 me=await ABH.get_me()
 x=me.id
 media=await ABH.download_media(input_link)
 sender=await event.get_sender()
 sender_id=event.sender_id
 ABH_date=event.date.strftime("%Y-%m-%d")
 ABH_day=ABH_Asbo3[event.date.strftime("%A")]
 await ABH.send_file(x,media,caption=caption,parse_mode="markdown")
 os.remove(media)
def joker_unread_media(message):
 return message.media_unread and (message.photo or message.video)
async def Hussein_event(event,caption):
 media=await event.download_media()
 sender=await event.get_sender()
 sender_id=event.sender_id
 ABH_date=event.date.strftime("%Y-%m-%d")
 ABH_day=ABH_Asbo3[event.date.strftime("%A")]
 await ABH.send_file("me",media,caption=caption,parse_mode="markdown")
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
