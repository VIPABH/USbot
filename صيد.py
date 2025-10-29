import asyncio
from telethon import events
from telethon.tl.functions.channels import JoinChannelRequest, CreateChannelRequest, UpdateUsernameRequest
from telethon.errors import UserAlreadyParticipantError
from ABH import ABH, r
CHANNELS = ['x04ou', 'sszxl', 'sizxll', 'ANYMOUSupdate']
RETRY_INTERVAL = 1200
hunt_task_running = False
async def join_required_channels():
    for c in CHANNELS:
        try:
            await ABH(JoinChannelRequest(c))
        except UserAlreadyParticipantError:
            continue
        except Exception:
            pass
async def attempt_hunt(user_id, username):
    try:
        await ABH.get_entity(username)
    except ValueError:
        await ABH.send_message('me', f'🎯 اليوزر متاح: {username}')
        try:
            result = await ABH(CreateChannelRequest(
                title="صيد اليوزرات 🚀",
                about="قناة تخزين اليوزرات المتاحة",
                megagroup=False
            ))
            new_channel = result.chats[0]
            await ABH(UpdateUsernameRequest(
                channel=new_channel,
                username=username.replace("@", "")
            ))
            await ABH.send_message('me', f'📌 تم إنشاء قناة بالمعرف: {username}')
            r.delete(f"صيد:{user_id}")
        except Exception as err:
            await ABH.send_message('me', f'⚠️ فشل تعيين المعرف {username}\n{err}\n⏳ سيعاد بعد 20 دقيقة.')
async def hunt_task():
    global hunt_task_running
    hunt_task_running = True
    await ABH.send_message('me', "🚀 تشغيل مهمة الصيد.")
    while True:
        keys = r.keys("صيد:*")
        if not keys:
            hunt_task_running = False
            await ABH.send_message('me', "🛑 تم إيقاف الصيد.")
            break
        await join_required_channels()
        for key in keys:
            user_id = key.decode().split(":")[1]
            username = r.get(key)
            if username:
                await attempt_hunt(user_id, username)
        await asyncio.sleep(RETRY_INTERVAL)
@ABH.on(events.NewMessage(pattern="^صيد (.+)$", outgoing=True))
async def save(e):
    user = e.pattern_match.group(1)
    if not user.startswith('@'):
        return await e.edit("❌ استخدم الأمر مثل: صيد @user")
    r.set(f"صيد:{e.sender_id}", user)
    await e.edit(f"✅ تم تخزين {user}، يبدأ الصيد كل 20 دقيقة.")
    global hunt_task_running
    if not hunt_task_running:
        ABH.loop.create_task(hunt_task())
@ABH.on(events.NewMessage(pattern="^(ايقاف صيد|ايقاف الصيد)$", outgoing=True))
async def stop(e):
    r.delete(f"صيد:{e.sender_id}")
    await e.edit("🛑 تم إيقاف الصيد.")
@ABH.on(events.NewMessage(pattern=r"^(يوزر الصيد|حالة الصيد)$", outgoing=True))
async def shows(e):
    x = r.get(f"صيد:{e.sender_id}")
    await e.edit(f"🎯 اليوزر الحالي: {x.decode() if x else 'لا يوجد صيد.'}")
