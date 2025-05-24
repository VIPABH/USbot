from telethon import events
from ABH import ABH
import asyncio
target_user_id = 1421907917
@ABH.on(events.NewMessage(pattern=r"^كلمات (\d+)$"))
async def words(event):
    if event.sender_id != target_user_id:
        return await event.reply(" هذا الأمر مخصص لمستخدم معين فقط.")
    num = int(event.pattern_match.group(1)) or 1
    await event.respond(" أرسل الكلمات المطلوبة الآن...")    
    async with ABH.conversation(event.chat_id, timeout=10) as conv:
        try:
            msg = await conv.get_response()
            if msg.sender_id != target_user_id:
                return
            text = msg.raw_text.strip()
            words = text.split()
            if len(words) < num:
                await event.respond(f" أرسلت فقط {len(words)} كلمة، بينما طلبت {num}.")
            else:
                await event.respond(f" تم استقبال {num} كلمة:\n" + "\n".join(words[:num]))
        except asyncio.TimeoutError:
            await event.respond(" لم يتم الرد في الوقت المحدد.")
