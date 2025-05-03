from ABH import ABH, gidvar, events #type: ignore
@ABH.on(events.NewMessage)
async def التخزين(event):
    r = await event.get_reply_message()
    text = event.text
    me = await ABH.get_me()
    if me.username and f"@{me.username}" in text:
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
