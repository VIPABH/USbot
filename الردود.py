import json, os
from telethon import events
from telethon.tl.types import ReactionEmoji
from telethon.tl.functions.messages import SendReactionRequest
from ABH import ABH

DATA_FILE = "reaction_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

reaction_data = load_data()

@ABH.on(events.NewMessage(pattern=r"^اضف (-?\d+)\s+(\S+)$", func=lambda e: e.out))
async def add_channel(event):
    chat_id = event.pattern_match.group(1)
    reaction = event.pattern_match.group(2)

    if not chat_id.startswith("-100"):
        return await event.reply("❌ هذا ليس آيدي قناة صالح!")

    # حفظ تفاعل واحد فقط
    reaction_data[chat_id] = {"reaction": reaction}
    save_data(reaction_data)

    await event.reply(f"✅ تمت إضافة `{chat_id}` مع التفاعل: {reaction}")

@ABH.on(events.NewMessage(pattern=r"^احذف (-?\d+)$", func=lambda e: e.out))
async def remove_channel(event):
    chat_id = event.pattern_match.group(1)
    if chat_id in reaction_data:
        del reaction_data[chat_id]
        save_data(reaction_data)
        await event.reply(f"🗑️ تم حذف القناة `{chat_id}` من التفاعلات.")
    else:
        await event.reply("⚠️ هذه القناة غير موجودة في القائمة.")

@ABH.on(events.NewMessage(pattern="^القنوات$", func=lambda e: e.out))
async def list_channels(event):
    if not reaction_data:
        return await event.reply("📭 لا توجد قنوات مضافة.")
    text = "📡 القنوات والتفاعلات:\n\n"
    for cid, data in reaction_data.items():
        text += f"• `{cid}` → {data.get('reaction')}\n"
    await event.reply(text)

@ABH.on(events.NewMessage)
async def auto_react(event):
    chat_id = str(event.chat_id)
    if event.is_channel and chat_id in reaction_data:
        reaction = reaction_data[chat_id].get("reaction")
        if not reaction:
            return
        try:
            await ABH(SendReactionRequest(
                peer=event.chat_id,
                msg_id=event.id,
                reaction=[ReactionEmoji(emoticon=reaction)]
            ))
        except:
            return