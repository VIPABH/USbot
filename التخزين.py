from telethon.tl.functions.channels import CreateChannelRequest
from telethon.tl.functions.users import GetFullUserRequest
from ABH import ABH, events  # type: ignore
from config import *  # type: ignore
from telethon.tl.types import User
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
    response = f'''فارات السورس
لا تحذف الرسالة للحفاظ على كروبات السورس
مجموعة التخزين gidvar:
{gidvar or "لم يتم العثور على الفار"}
مجموعة الإشعارات hidvar:
{hidvar or "لم يتم العثور على الفار"}
'''
    await ABH.send_message(me.id, response)
@ABH.on(events.NewMessage())
async def gidvar_save(event):
    if not gidvar:
        await config_vars(event)    
    sender = await event.get_sender()
    me = await ABH.get_me()
    text = event.text
    uid = event.sender_id
    if not event.is_private or uid == me.id or uid == 777000 or sender.bot:
        return
    name = sender.first_name
    await ABH.send_message(
        int(gidvar),
    f'''
المستخدم : {name}

رسالته : {text}

ايديه : `{uid}`
''')
    await event.forward_to(int(gidvar))
    oid = me.id
    print(oid)
    text = event.text
    print(text)
    if oid in text:
        chat = await event.get_chat()
        name = sender.first_name if isinstance(sender, User) else "غير معروف"
        gid = str(chat.id).replace("-100", "")
        msg_id = event.id
        await ABH.send_message(
            int(gidvar),
            f"""#التــاكــات
⌔┊الكــروب : {chat.title}

⌔┊المـرسـل : {name}

⌔┊الرســالـه : {text}

⌔┊رابـط الرسـاله : [link](https://t.me/c/{gid}/{msg_id})
""",
link_preview=False
        )
print("التخزين شغال")
