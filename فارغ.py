from telethon import events
from ABH import *
@ABH.on(events.NewMessage(pattern="^mx$", outgoing=True))
async def mx(event):
    await event.edit("جاري الفحص...")
    for i in range(385, 432):
        msg = ""
        x = await ABH.get_message("x04ou", i)
        if x:
            msg += f'{i} موجود\n'
        else:
            msg += f'{i} غير موجود\n'
    await event.edit(msg)
