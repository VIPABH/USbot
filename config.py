from datetime import datetime
from telethon import events
from ABH import ABH
now = datetime.now()
تاريخ = now.strftime("%Y-%m-%d")
ساعة = now.strftime("%I:%M:%S %p")
وقت_بدء_التشغيل = datetime.now()
@ABH.on(events.NewMessage(pattern="^.فحص|فحص", outgoing=True))
async def testup(event):
    الآن = datetime.now()
    مدة_التشغيل = الآن - وقت_بدء_التشغيل
    التاريخ = الآن.strftime("%Y-%m-%d")
    الساعة = الآن.strftime("%I:%M:%S %p")
    start = datetime.now()
    await event.edit("**᯽︙ جـاري فـحص الـبـوت**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    cap = (
        f"**᯽︙ السورس شغال**\n"
        f"᯽︙ **الـتـاريخ:** `{التاريخ}`\n"
        f"᯽︙ **الـسـاعه:** `{الساعة}`\n"
        f"᯽︙ **شغال من:** `{مدة_التشغيل}`\n"
        f"᯽︙ **الـزمن:** `{ms} ms`\n"
        f"᯽︙ **الـبـوت شغال 100%**"
    )
    await event.delete()
    pic = 'https://files.catbox.moe/ebn0d8.jpg'
    await event.respond(file=pic, message=cap)
