from ABH import *
from telethon import events
from telethon.tl.types import ReactionEmoji
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
@ABH.on(events.NewMessage)
async def auto_react(event):
    c = await event.get_chat()
    if event.is_privte:
        return
    else:
        if c.id in x:
            await ABH(SendReactionRequest(
                peer=event.chat_id,
                msg_id=event.id,
                reaction=[ReactionEmoji(emoticon=p)]
    ))
    