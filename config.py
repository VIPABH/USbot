from datetime import datetime
from telethon import events
from ABH import *
now = datetime.now()
تاريخ= now.strftime("%Y-%m-%d")
ساعة = now.strftime("%I:%M:%S %p")
@ABH(events.NewMessage(pattern="^فحص$", outgoing=True))
async def testup(event):
    now = datetime.now()
    التاريخ = now.strftime("%Y-%m-%d")
    السااعة = now.strftime("%I:%M:%S %p")
    start = datetime.now()
    await event.edit("**᯽︙ جـاري فـحص الـبـوت**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f"**᯽︙ السورس شغال**\n᯽︙ **الـتـاريخ ** `{التاريخ}`\n᯽︙ **الـسـاعه :** `{السااعة}`\n᯽︙ **الـزمن :** `{ms} ms` \n᯽︙ **تاريخ التشغيل :** `{تاريخ}`\n᯽︙ **ساعة التشغيل :** `{ساعة}`\n᯽︙ **الـبـوت شغال 100%**")
