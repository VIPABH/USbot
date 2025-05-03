from telethon.tl.functions.channels import CreateChannelRequest
from ABH import ABH, events  # type: ignore
from config import *  # type: ignore
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
    try:
        if not gidvar:
            await config_vars(event)
        me = await ABH.get_me()
        text = event.text or ""
        main_username = me.username
        alt_usernames = [u.username for u in me.usernames] if me.usernames else []
        usernames_to_check = [main_username] if main_username else []
        usernames_to_check += alt_usernames
        if any(username and username in text for username in usernames_to_check):
            chat = await event.get_chat()
            gid = str(chat.id).replace("-100", "")
            msg_id = event.id
            await ABH.send_message(
                int(gidvar),
                f'''#التــاكــات
الرسالة : {text}
⌔┊رابـط الرسـاله : [link](https://t.me/c/{gid}/{msg_id})''',
                link_preview=False,
                parse_mode="markdown"
            )
    except Exception as e:
        print(f"[تحذير] حدث خطأ في gidvar_save: {e}")
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
'''
    )
