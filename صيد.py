import asyncio
from telethon import events
from telethon.tl.functions.channels import JoinChannelRequest, CreateChannelRequest, UpdateUsernameRequest
from telethon.errors import UserAlreadyParticipantError
from ABH import ABH, r
CHANNELS = ['x04ou', 'sszxl', 'sizxll', 'ANYMOUSupdate']
RETRY_INTERVAL = 1200  
hunt_task_handle = None 
async def join_required_channels():
    for c in CHANNELS:
        try:
            await ABH(JoinChannelRequest(c))
        except UserAlreadyParticipantError:
            continue
        except Exception as e:
            print(f"خطأ بالانضمام للقناة {c}: {e}")
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
    """تنفيذ مهمة الصيد لجميع اليوزرات المخزنة مرة واحدة"""
    keys = r.keys("صيد:*")
    if not keys:
        return False
    await join_required_channels()
    for key in keys:
        user_id = key.decode().split(":")[1]
        username = r.get(key)
        if username:
            await attempt_hunt(user_id, username)
    return True
async def periodic_hunt():
    """تشغيل مهمة الصيد بشكل دوري كل 20 دقيقة إذا كان هناك يوزرات"""
    global hunt_task_handle
    while True:
        has_users = await hunt_task()
        if not has_users:
            hunt_task_handle = None
            break
        await asyncio.sleep(RETRY_INTERVAL)
@ABH.on(events.NewMessage(pattern="^صيد (.+)$", outgoing=True))
async def save(e):
    global hunt_task_handle
    user = e.pattern_match.group(1)
    if not user.startswith('@'):
        return await e.edit("❌ استخدم الأمر مثل: صيد @user")
    r.set(f"صيد:{e.sender_id}", user)
    await e.edit(f"✅ تم تخزين {user}، )
    if not hunt_task_handle:
        hunt_task_handle = ABH.loop.create_task(periodic_hunt())
@ABH.on(events.NewMessage(pattern="^(ايقاف صيد|ايقاف الصيد)$", outgoing=True))
async def stop(e):
    r.delete(f"صيد:{e.sender_id}")
    await e.edit("🛑 تم إيقاف الصيد.")
@ABH.on(events.NewMessage(pattern=r"^(يوزر الصيد|حالة الصيد)$", outgoing=True))
async def shows(e):
    x = r.get(f"صيد:{e.sender_id}")
    await e.edit(f"🎯 اليوزر الحالي: {x.decode() if x else 'لا يوجد صيد.'}")
