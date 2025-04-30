from telethon import TelegramClient, events
import asyncio, os

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# تأكيد أن القيم موجودة
if not api_id or not api_hash:
    raise ValueError("يجب تعيين API_ID و API_HASH كمتغيرات بيئية.")

# إنشاء عميل يوزر بوت
ABH = TelegramClient('session', int(api_id), api_hash)

@ABH.on(events.NewMessage(pattern='خاص'))
async def save(event):
    uid = event.sender_id
    me = await ABH.get_me()
    r = await event.get_reply_message()

    # تحقق من وجود رد
    if not r:
        try:
            await event.reply('🤔 يجب أن ترد على رسالة.')
            await asyncio.sleep(3)
            await event.delete()
        except:
            pass
        return

    # إذا كانت الرسالة من نفسك (يعني تعمل كيوزر بوت)
    if uid == me.id:
        try:
            await ABH.forward_messages(me.id, r)
            await asyncio.sleep(3)
            await event.delete()
        except Exception as e:
            await event.reply(f"حدث خطأ: {e}")
    else:
        await asyncio.sleep(1)
        await event.delete()

# تشغيل اليوزر بوت
async def main():
    await ABH.start()
    print("✅ تم تسجيل الدخول كـ Userbot.")
    await ABH.run_until_disconnected()

asyncio.run(main())
