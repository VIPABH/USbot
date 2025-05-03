from ABH import ABH, events #type: ignore
from config import * #type: ignore
print(gidvar)
print(hidvar)
@ABH.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def gidvar_save(event):
    sender = await event.get_sender()
    bot = sender.bot
    chat = event.chat_id
    if bot or chat == gidvar or chat == 777000:
        return
    text = event.text
    me = await ABH.get_me()
    if me.username and f"@{me.username}" in text or is:
          cid = await event.get_chat()
          sender = await event.get_sender()
          chat_id_str = str(cid.id).replace("-100", "")
          msg_id = event.id
          await ABH.send_message(
          gidvar,
            f"""
#التــاكــات

⌔┊الكــروب : {cid.title if hasattr(cid, 'title') else 'خاص'}

⌔┊المرسل :  {sender.first_name}

⌔┊الرســالـه : {text}

⌔┊رابـط الرسـاله : [link](https://t.me/c/{chat_id_str}/{msg_id})
""",
            link_preview=False
        )
print("التخزين شغال")
