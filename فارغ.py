from telethon.tl.functions.channels import CreateChannelRequest, UpdateUsernameRequest
from telethon import events
from ABH import *
@ABH.on(events.NewMessage(pattern="^صيد (.+)$", outgoing=True))
async def save(e):
    user = e.pattern_match.group(1)
    if not user or not user.startswith('@'):
        await e.edit('عذرا بس الامر يعمل ك صيد @wfffp')
        return
    r.set(f"صيد:{e.sender_id}", user)
    await e.edit(f'تم تخزين {user} للصيد')
@ABH.on(events.NewMessage)
async def h(e):
    x = r.get(f"صيد:{e.sender_id}")
    if not x:
        return
    try:
        z = await ABH.get_entity(x)
    except ValueError:
        await ABH.send_message('me', f'اليوزر متاح {x}')
        result = await ABH(CreateChannelRequest(
        title="صيد اليوزرات 🚀",
        about="قناة تخزين اليوزرات المتاحة",
        megagroup=False
        ))
        new_channel = result.chats[0]
        try:
            await ABH(UpdateUsernameRequest(
                channel=new_channel,
                username=x.replace("@", "")
            ))
            await ABH.send_message('me', f'📌 تم إنشاء قناة وتعيين معرفها: {x}')
            r.delete(f"صيد:{e.sender_id}")
        except Exception as err:
            await ABH.send_message(
                'me',
                f'⚠️ فشل تعيين المعرف \n من الممكن الخطأ بسبب عدد القنوات لديك 20 احذف واحده {x}: {err}')
@ABH.on(events.NewMessage(pattern="^(ايقاف صيد|ايقاف الصيد)$", outgoing=True))
async def stop(e):
    await e.edit('تم ايقاف الصيد بنجاح')
    r.delete(f"صيد:{e.sender_id}")
