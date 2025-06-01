from ABH import *
from telethon import events
x = ()
@ABH.on(events.NewMessage(pattern="اضف قناة تفاعل (.+)"))
async def add_ch(event):
    ch = event.pattern_match.group(1)
    if ch.startswith("-100"):
        x.add(ch)
        await event.reply("تم إضافة القناة بنجاح!")
    else:
        await event.reply("هذا ليس آيدي قناة!!")
        return
@ABH.on(events.Newmessage(pattern="القنوات"))
async def show(event)
    await event.reply(x)