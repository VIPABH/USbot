from telethon import events
from ABH import ABH
import asyncio, re
target_user_id = 1421907917
@ABH.on(events.NewMessage(pattern=r"^كلمات (\d+)$", outgoing=True))
async def words(event):
    await event.delete()
    num = int(event.pattern_match.group(1)) or 1
    for i in range(num):
        async with ABH.conversation(event.chat_id, timeout=10) as conv:
            await conv.send_message("كلمات")
            try:
                while True:
                    msg = await conv.get_response()
                    if msg.sender_id != target_user_id:
                        continue
                    text = msg.raw_text.strip()
                    text = msg.raw_text.strip()
                    match = re.search(r"\(\s*(.+?)\s*\)", text)
                    if match:
                        text = match.group(1)
                        await conv.send_message(text)
                    break
            except asyncio.TimeoutError:
                return
