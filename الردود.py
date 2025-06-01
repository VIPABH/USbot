from ABH import *
from telethon import events
x = ()
@ABH.on(events.NewMessage(pattern="اضف قناة تفاعل (.+)"))
async def add_ch(event)
    ch = event.pattern.match.group(2)
    if ch.startwith("-100"):
        x.add(ch)
    else:
        await event.reply("هذا مو ايدي قناة!!")
        return