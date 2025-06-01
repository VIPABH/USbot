from ABH import ABH
from telethon import events
from telethon.tl.types import ReactionEmoji
from telethon.tl.functions.messages import SendReactionRequest

# قائمة القنوات التي سيتم التفاعل معها تلقائيًا
reaction_channels = set()

# إضافة قناة إلى قائمة التفاعل
@ABH.on(events.NewMessage(pattern=r"اضف (-?\d+)"))
async def add_channel(event):
    chat_id = int(event.pattern_match.group(1))
    if str(chat_id).startswith("-100"):
        reaction_channels.add(chat_id)
        await event.respond("✅ تم إضافة القناة إلى قائمة التفاعل التلقائي.")
    else:
        await event.respond("❌ هذا ليس آيدي قناة صالح!")

# عرض القنوات المضافة
@ABH.on(events.NewMessage(pattern="^القنوات$"))
async def list_channels(event):
    if not reaction_channels:
        await event.respond("🚫 لا توجد قنوات مضافة حتى الآن.")
    else:
        channels_list = "\n".join(str(cid) for cid in reaction_channels)
        await event.respond(f"📡 القنوات المضافة:\n{channels_list}")

# التفاعل تلقائيًا مع الرسائل في القنوات المحددة
@ABH.on(events.NewMessage)
async def auto_react(event):
    if event.is_channel and event.chat_id in reaction_channels:
        try:
            await ABH(SendReactionRequest(
                peer=event.chat_id,
                msg_id=event.id,
                reaction=[ReactionEmoji(emoticon="👍")]
            ))
        except Exception as e:
            print(f"خطأ في إرسال التفاعل: {e}")