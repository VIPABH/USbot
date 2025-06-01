from ABH import *
from telethon import events
x = set()
@ABH.on(events.NewMessage(pattern="اضف قناة تفاعل (.+)"))
async def add_ch(event):
    ch = event.pattern_match.group(1)
    if ch.startswith("-100"):
        x.add(ch)
        await event.edit("تم إضافة القناة بنجاح!")
    else:
        await event.edit("هذا ليس آيدي قناة!!")
        return
@ABH.on(events.NewMessage(pattern="القنوات"))
async def show(event):
    await event.edit(f"{x}")
