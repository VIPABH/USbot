from telethon import events
from ABH import ABH
import asyncio
target_user_id = 1421907917
@ABH.on(events.NewMessage(pattern=r"^كلمات (\d+)$"))
async def words(event):
    async with ABH.conversation(event.chat_id, timeout=60) as conv:
        await conv.send_message("كلمات")
        try:
            while True:
                msg = await conv.get_response()
                if msg.sender_id != target_user_id:
                    continue
                text = msg.raw_text.strip()
                await conv.send_message(f" تم استقبال النص:\n{text}")
                break
        except asyncio.TimeoutError:
            await conv.send_message(" لم يتم الرد خلال المهلة المحددة.")
