import json,os
from telethon import events
from telethon.tl.types import ReactionEmoji
from telethon.tl.functions.messages import SendReactionRequest
from ABH import ABH

DATA_FILE="reaction_data.json"

def load_data():
 if not os.path.exists(DATA_FILE):return{}
 with open(DATA_FILE,"r",encoding="utf-8") as f:return json.load(f)

def save_data(data):
 with open(DATA_FILE,"w",encoding="utf-8") as f:json.dump(data,f,ensure_ascii=False,indent=2)

reaction_data=load_data()

@ABH.on(events.NewMessage(pattern=r"^اضف (-?\d+)\s+(.+)$",func=lambda e:e.out))
async def add_channel(event):
 chat_id=event.pattern_match.group(1)
 reactions=event.pattern_match.group(2).split()
 if not chat_id.startswith("-100"):return await event.reply("❌هذا ليس آيدي قناة صالح!")
 if len(reactions)>3:return await event.reply("❌يمكنك إضافة 3 تفاعلات كحد أقصى لكل قناة.")
 reaction_data[chat_id]=reactions
 save_data(reaction_data)
 await event.reply(f"✅تم إضافة القناة `{chat_id}` مع التفاعلات: {' '.join(reactions)}")

@ABH.on(events.NewMessage(pattern=r"^احذف (-?\d+)$",func=lambda e:e.out))
async def remove_channel(event):
 chat_id=event.pattern_match.group(1)
 if chat_id in reaction_data:
  del reaction_data[chat_id]
  save_data(reaction_data)
  await event.reply(f"🗑️تم حذف القناة `{chat_id}` من التفاعلات.")
 else:await event.reply("⚠️هذه القناة غير موجودة في القائمة.")

@ABH.on(events.NewMessage(pattern="^القنوات$",func=lambda e:e.out))
async def list_channels(event):
 if not reaction_data:return await event.reply("📭لا توجد قنوات مضافة.")
 text="📡القنوات والتفاعلات:\n\n"
 for cid,reacts in reaction_data.items():text+=f"• `{cid}` → {' '.join(reacts)}\n"
 await event.reply(text)

@ABH.on(events.NewMessage)
async def auto_react(event):
 chat_id=str(event.chat_id)
 if event.is_channel and chat_id in reaction_data:
  for emoji in reaction_data[chat_id]:
   try:
    await ABH(SendReactionRequest(
     peer=event.chat_id,
     msg_id=event.id,
     reaction=[ReactionEmoji(emoticon=emoji)]
    ))
   except Exception as e:print(f"⚠️خطأ في إرسال التفاعل {emoji}: {e}")