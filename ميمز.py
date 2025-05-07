from ABH import ABH, ok, events #type:ignore
@ok
@ABH.on(events.NewMessage(pattern='^الميمز$', outgoing=True))
async def list(event):
    await event.edit(
        '''᯽︙ قائمة تخزين اوامر الميمز:
البصمة : `اللهي`
البصمة : `سيد`
البصمة : `ايرور`
البصمة : `نيو`
البصمة : `انجب`
البصمة : `ماذا`
البصمة : `يولن`
البصمة : `هه`
البصمة : `لاا`
البصمة : `مرهم`
البصمة : `لتكفرونه`
البصمة : `وخر`
البصمة : `اش`
البصمة : `انعل`
البصمة : `طاح`
البصمة : `لب`
البصمة : `صل`
البصمة : `فد`
البصمة : `نعل`
البصمة : `الماوارثها`
البصمة : `يدكتور`
البصمة : `امريكا`
البصمة : `هاا`
البصمة : `مي`
البصمة : `ببج`
البصمة : `فلا`
البصمة : `تف`
البصمة : `شيله عبود`
البصمة : `ههه`
البصمة : `صلاة`
البصمة : `زيج`
البصمة : `الكعبة`
''')
@ok
@ABH.on(events.NewMessage(pattern='^اللهي$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/23"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^سيد$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/16"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^ايرور$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/7"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^نيو$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/5"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^انجب$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/79"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^ماذا$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/81"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^يولن$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/292"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^هه$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/338"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^لاا$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/535"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^مرهم$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/537"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^لتكفرونه$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/571"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^وخر$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/589"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^اش$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/592"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^انعل$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/597"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^طاح$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/612"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^لب$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/614"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^صل$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/735"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^فد$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/748"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^نعل$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/1008"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^الماوارثها$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/VIPABH/1093"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^يدكتور$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/VIPABH/1107"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^نوكيا$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/VIPABH/1111"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^امريكا$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/VIPABH/1113"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^هاا$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/VIPABH/1115"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^مي$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/VIPABH/1116"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^ببج$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/VIPABH/1134"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^فلا$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/VIPABH/1160"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^تف$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/VIPABH/1161"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^شيله عبود$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/VIPABH/1162"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^ههه$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/VIPABH/1164"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^صلاة$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/VIPABH/1187"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^زيج$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/VIPABH/1206"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
@ok
@ABH.on(events.NewMessage(pattern='^الكعبة$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/VIPABH/1207"
    await ABH.send_file(event.chat_id, url, reply_to=r.id)
