from ABH import ABH, events  # type: ignore
from config import *  # type: ignore
import os
ABH_Asbo3 = {
    'Monday': 'الاثنين',
    'Tuesday': 'الثلاثاء',
    'Wednesday': 'الأربعاء',
    'Thursday': 'الخميس',
    'Friday': 'الجمعة',
    'Saturday': 'السبت',
    'Sunday': 'الأحد'
}
@ABH.on(events.NewMessage(pattern="^جلب$", outgoing=True))
async def dato(event):
    if not event.is_reply:
        await event.edit("🤔 يجب أن ترد على صورة أو وسائط لحفظها.")
        await asyncio.sleep(3)
        await event.delete()
        return
    sender = await event.get_sender()
    reply = await event.get_reply_message()

    if not reply.media:
        await event.delete()
        return
    media = await reply.download_media()
    await event.client.send_file(
        sender.id,
        media,
        caption="- تـم حفظ الصـورة بنجـاح ✓"
    )
    await event.delete()
async def Hussein(event, caption):
    media = await event.download_media()
    sender = await event.get_sender()
    sender_id = event.sender_id
    ABH_date = event.date.strftime("%Y-%m-%d")
    ABH_day = ABH_Asbo3[event.date.strftime("%A")]
    await ABH.send_file(
        "me",
        media,
        caption=caption.format(sender.first_name, sender_id, ABH_date, ABH_day),
        parse_mode="markdown"
    )
def joker_unread_media(message):
    return message.media_unread and (message.photo or message.video)
async def Hussein(event, caption):
    media = await event.download_media()
    sender = await event.get_sender()
    sender_id = event.sender_id
    ABH_date = event.date.strftime("%Y-%m-%d")
    ABH_day = ABH_Asbo3[event.date.strftime("%A")]
    await ABH.send_file(
        "me",
        media,
        caption=caption.format(sender.first_name, sender_id, ABH_date, ABH_day),
        parse_mode="markdown"
    )
    os.remove(media)
@ABH.on(events.NewMessage(func=lambda e: e.is_private and joker_unread_media(e)))
async def Reda(event):
       a = event.sender.first_name
       b = event.sender_id
       c = event.date.strftime("%Y-%m-%d")
       d = ABH_Asbo3[event.date.strftime("%A")]
       caption = f"""**
       ♡ تم حفظ الذاتية بنجاح ✓
♡ أسم المرسل : [{a}](tg://user?id={b})
♡  تاريخ الذاتية : `{c}`
♡  أرسلت في يوم `{d}`
       ♡    ABH    ♡
        **"""
       await Hussein(event, caption)
