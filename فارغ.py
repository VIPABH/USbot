from telethon import events
from ABH import *
@ABH.on(events.NewMessage(pattern="^صيد (.+)$", outgoing=True))
async def save(e):
    user = e.pattern_match.group(1)
    if not user or not user.startswith('@'):
        await e.edit('عذرا بس الامر يعمل ك صيد @wfffp')
        return
    r.set(f"صيد:{e.sender_id}", user)
    await e.reply(f'تم تخزين {user} للصيد')
@ABH.on(events.NewMessage)
async def h(e):
    x = r.get(f"صيد:{e.sender_id}")
    if not x:
        return
    z = await ABH.get_entity(x)
    if not z:
        await ABH.send_message('me', f'اليوزر متاح {x}')
