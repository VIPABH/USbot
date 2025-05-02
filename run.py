# from telethon.tl.functions.messages import CreateChannelRequest
from ABH import ABH, events, ok #type: ignore
import asyncio, re
async def create_group(name, about):
    result = await ABH(CreateChannelRequest(
        title=name,
        about=about,
        megagroup=True
    ))
    group = result.chats[0]
    return group.id, group.title
@ABH.on(events.NewMessage(pattern='/config'))
async def config_vars(event):
    me = await ABH.get_me()
    gidvar_value = None
    hidvar_value = None
    async for msg in ABH.iter_messages(me.id):
        if not msg.text:
            continue
        gid_match = re.search(r'gidvar:\s*(.+)', msg.text, re.IGNORECASE)
        hid_match = re.search(r'hidvar:\s*(.+)', msg.text, re.IGNORECASE)
        if gid_match and not gidvar_value:
            gidvar_value = gid_match.group(1).strip()
        if hid_match and not hidvar_value:
            hidvar_value = hid_match.group(1).strip()
        if gidvar_value and hidvar_value:
            break
    newly_created = []
    if not gidvar_value:
        gidvar_value, gid_name = await create_group("مجموعة التخزين", "هذه المجموعة مخصصة لتخزين البيانات.")
        newly_created.append(("مجموعة التخزين", gidvar_value))
    if not hidvar_value:
        hidvar_value, hid_name = await create_group("مجموعة الإشعارات", "هذه المجموعة مخصصة للتنبيهات.")
        newly_created.append(("مجموعة الإشعارات", hidvar_value))
    if newly_created:
        config_text = f'''#فارات السورس
لا تحذف الرسالة للحفاظ على كروبات السورس

مجموعة التخزين gidvar: {gidvar_value}
مجموعة الإشعارات hidvar: {hidvar_value}
        '''
        await ABH.send_message(me.id, config_text)
        ids_text = "تم إنشاء الكروبات التالية:\n\n"
        for title, gid in newly_created:
            ids_text += f"**{title}**\nID: `{gid}`\n\n"
        await ABH.send_message(me.id, ids_text)
    response = f'''#فارات السورس
لا تحذف الرسالة للحفاظ على كروبات السورس
مجموعة التخزين gidvar:
{gidvar_value or " لم يتم العثور على الفار"}
مجموعة الإشعارات hidvar:
{hidvar_value or " لم يتم العثور على الفار"}
    '''
    await event.reply(response)
