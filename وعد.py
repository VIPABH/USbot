from telethon import events
from ABH import ABH
import asyncio
target_user_id = 1421907917
@ABH.on(events.NewMessage(pattern=r"^كلمات (\d+)$"))
async def words(event):
    if not event.out:
        return
    num = int(event.pattern_match.group(1)) or 1
    async with ABH.conversation(event.chat_id, timeout=60) as conv:
        await conv.send_message("✏️ أرسل الكلمات المطلوبة الآن...")
        try:
            while True:
                msg = await conv.get_response()
                if msg.sender_id != target_user_id:
                    await msg.reply(" هذه الرسالة ليست من المستخدم المطلوب.")
                    continue
                text = msg.raw_text.strip()
                words = text.split()
                if len(words) < num:
                    await event.respond(f" أرسلت فقط {len(words)} كلمة، بينما طلبت {num}.")
                else:
                    await event.respond(f" تم استقبال {num} كلمة:\n" + "\n".join(words[:num]))
                break
        except asyncio.TimeoutError:
            await event.respond(" لم يتم الرد خلال المهلة المحددة.")
