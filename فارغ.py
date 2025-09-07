from telethon import events
from ABH import *
@ABH.on(events.NewMessage(pattern="^mx$", outgoing=True))
async def mx(event):
    await event.edit("جاري الفحص...")
    msg = ""
    for i in range(385, 432):
        x = await ABH.get_messages("x04ou", ids=i)
        if x:
            msg += f'{i} موجود\n'
        else:
            msg += f'{i} غير موجود\n'
    await event.edit(msg)
