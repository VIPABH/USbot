from ABH import ABH, events #type: ignore
from config import * #type: ignore
print(gidvar)
print(hidvar)
@ABH.on(events.NewMessage(incoming=True, func=lambda e: e.is_reply or e.raw_text))
async def gidvar_save(event):
    sender = await event.get_sender()
    if sender.bot or event.chat_id in (gidvar, 777000):
        return
    text = event.raw_text
    me = await ABH.get_me()
    replied = await event.get_reply_message()
    if (
        (me.username and f"@{me.username}" in text) or
        (str(me.id) in text) or
        (replied and replied.sender_id == me.id)
    ):
        chat = await event.get_chat()
        chat_id_str = str(chat.id).replace("-100", "")
        msg_id = event.id
        await ABH.send_message(
            gidvar,
            f"""
#التــاكــات

⌔┊الكــروب : {chat.title if hasattr(chat, 'title') else 'خاص'}

⌔┊المرسل : {sender.first_name}

⌔┊الرســالـه : {text}

⌔┊رابـط الرسـاله : [link](https://t.me/c/{chat_id_str}/{msg_id})
            """,
            link_preview=False
        )
print("التخزين شغال")
