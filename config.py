from datetime import datetime
from telethon import events
from ABH import ABH
now = datetime.now()
تاريخ = now.strftime("%Y-%m-%d")
ساعة = now.strftime("%I:%M:%S %p")
@ABH.on(events.NewMessage(pattern="^فحص$", outgoing=True))
async def testup(event):
    now = datetime.now()
    التاريخ = now.strftime("%Y-%m-%d")
    السااعة = now.strftime("%I:%M:%S %p")
    start = datetime.now()
    await event.edit("**᯽︙ جـاري فـحص الـبـوت**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    cap = (
        f"**᯽︙ السورس شغال**\n"
        f"᯽︙ **الـتـاريخ:** `{التاريخ}`\n"
        f"᯽︙ **الـسـاعه:** `{السااعة}`\n"
        f"᯽︙ **الـزمن:** `{ms} ms`\n"
        f"᯽︙ **تاريخ التشغيل:** `{تاريخ}`\n"
        f"᯽︙ **ساعة التشغيل:** `{ساعة}`\n"
        f"᯽︙ **الـبـوت شغال 100%**"
    )
    await event.delete()
    pic = 'https://files.catbox.moe/kvonq7'
    await event.respond(file=pic, caption=cap)
