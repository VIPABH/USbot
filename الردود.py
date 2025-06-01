from ABH import ABH
from telethon import events
from telethon.tl.types import ReactionEmoji
from telethon.tl.functions.messages import SendReactionRequest
reaction_channels = set()
@ABH.on(events.NewMessage(pattern=r"اضف قناة تفاعل (-?\d+)"))
async def add_channel(event):
    chat_id = int(event.pattern_match.group(1))
    if str(chat_id).startswith("-100"):
        reaction_channels.add(chat_id)
        await event.respond("✅ تم إضافة القناة إلى قائمة التفاعل التلقائي.")
    else:
        await event.respond("❌ هذا ليس آيدي قناة صالح!")
@ABH.on(events.NewMessage(pattern="القنوات"))
async def list_channels(event):
    if not reaction_channels:
        await event.edit("🚫 لا توجد قنوات مضافة حتى الآن.")
    else:
        channels_list = "\n".join(str(cid) for cid in reaction_channels)
        await event.edit(f"📡 القنوات المضافة:\n{channels_list}")
@ABH.on(events.NewMessage)
async def auto_react(event):
    chat = await event.get_chat()
    if chat.id in reaction_channels:
        await ABH(SendReactionRequest(
            peer=event.chat_id,
            msg_id=event.id,
            reaction=[ReactionEmoji(emoticon="👍")]
            ))
