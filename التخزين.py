from telethon.tl.functions.channels import CreateChannelRequest
from ABH import ABH, events  # type: ignore
import re
gidvar = None
hidvar = None
async def create_group(name, about):
    result = await ABH(CreateChannelRequest(title=name, about=about, megagroup=True))
    group = result.chats[0]
    return group.id, group.title
@ABH.on(events.NewMessage(pattern='/config'))
async def config_vars(event):
    global gidvar, hidvar
    me = await ABH.get_me()
    async for msg in ABH.iter_messages(me.id):
        if not msg.text:
            continue
        gid_match = re.search(r'gidvar:\s*(.+)', msg.text, re.IGNORECASE)
        hid_match = re.search(r'hidvar:\s*(.+)', msg.text, re.IGNORECASE)
        if gid_match and not gidvar:
            gidvar = gid_match.group(1).strip()
        if hid_match and not hidvar:
            hidvar = hid_match.group(1).strip()
        if gidvar and hidvar:
            break
    newly_created = []
    if not gidvar:
        gidvar, gid_name = await create_group("مجموعة التخزين", "هذه المجموعة مخصصة لتخزين البيانات.")
        newly_created.append(("مجموعة التخزين", gidvar))
    if not hidvar:
        hidvar, hid_name = await create_group("مجموعة الإشعارات", "هذه المجموعة مخصصة للتنبيهات.")
        newly_created.append(("مجموعة الإشعارات", hidvar))
    if newly_created:
        config_text = f'''فارات السورس
لا تحذف الرسالة للحفاظ على كروبات السورس
مجموعة التخزين gidvar: {gidvar}
مجموعة الإشعارات hidvar: {hidvar}
'''
        await ABH.send_message(me.id, config_text)
        ids_text = "تم إنشاء الكروبات التالية:\n\n"
        for title, gid in newly_created:
            ids_text += f"**{title}**\nID: `{gid}`\n\n"
        await ABH.send_message(me.id, ids_text)
    print(f'hid = {hidvar}')
    print(f'gid = {gidvar}')
@ABH.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def privte_save(event):
    uid = event.sender_id
    s = await event.get_sender()
    if uid == 777000 or s.bot:
        return
    if not gidvar and hidvar:
        await config_vars(event)
    s = await event.get_sender()
    text = event.raw_text
    name = s.first_name or s.username or "Unknown"
    await ABH.send_message(
        int(gidvar), 
f'''المرسل : {name}

ايديه : `{uid}`

ارسل : {text}
''')
    m = event.message.id
    if not m:
        return
    await ABH.forward_messages(
        entity=int(gidvar),
        messages=m,
        from_peer=event.chat_id
    )
@ABH.on(events.NewMessage(incoming=True, func=lambda e: e.mentioned))
async def group_save(event):
    if not gidvar and hidvar:
        print("gidvar not found")
        await config_vars(event)
    uid = event.sender_id
    sender = await event.get_sender()
    if uid == 777000 or sender.bot:
        return
    s = await event.get_sender()
    gid = event.chat_id
    gid = str(gid).replace("-100", "").replace(" ", "")
    name = s.first_name or s.username or "Unknown"
    await ABH.send_message(
        int(gidvar),
f'''#التــاكــات

⌔┊الكــروب : {event.chat.title}

⌔┊المـرسـل :  {name}

⌔┊الرســالـه : {event.message.text}

⌔┊رابـط الرسـاله :  [link](https://t.me/c/{gid}/{event.message.id})
''')
    await ABH.forward_messages(
        entity=int(gidvar),
        messages=event.message.id,
        from_peer=event.chat_id
    )
    HVAR = hidvar
    GVAR = gidvar
