from telethon import events
from ABH import ABH
import asyncio, re
target_user_id = 1421907917
@ABH.on(events.NewMessage(pattern=r"^.كلمات (\d+)$", outgoing=True))
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
                    match = re.search(r"\(\s*(.+?)\s*\)", text)
                    if match:
                        text = match.group(1)
                        await conv.send_message(text)
                    break
            except asyncio.TimeoutError:
                return
target_user_id = 1421907917
@ABH.on(events.NewMessage(pattern=r"^.تركيب (\d+)$", outgoing=True))
async def words(event):
    await event.delete()
    num = int(event.pattern_match.group(1)) or 1
    for i in range(num):
        async with ABH.conversation(event.chat_id, timeout=10) as conv:
            await conv.send_message("تركيب")
            try:
                while True:
                    msg = await conv.get_response()
                    if msg.sender_id != target_user_id:
                        continue
                    text = msg.raw_text.strip()
                    match = re.search(r"\(\s*(.+?)\s*\)", text)
                    if match:
                        text = match.group(1)
                        merged = ''.join(text.split())
                        await conv.send_message(merged)
                    break
            except asyncio.TimeoutError:
                return
@ABH.on(events.NewMessage(pattern=r"^.تفكيك (\d+)$", outgoing=True))
async def words(event):
    await event.delete()
    num = int(event.pattern_match.group(1)) or 1
    for i in range(num):
        async with ABH.conversation(event.chat_id, timeout=10) as conv:
            await conv.send_message("تفكيك")
            try:
                while True:
                    msg = await conv.get_response()
                    if msg.sender_id != target_user_id:
                        continue
                    text = msg.raw_text.strip()
                    match = re.search(r"\(\s*(.+?)\s*\)", text)
                    if match:
                        text = match.group(1)
                        clean = ''.join(text.split())
                        separated = ' '.join(clean)
                        await conv.send_message(separated)
                    break
            except asyncio.TimeoutError:
                return
@ABH.on(events.NewMessage(pattern=r"^.احسب (\d+)$", outgoing=True))
async def words(event):
    await event.delete()
    num = int(event.pattern_match.group(1)) or 1
    for _ in range(num):
        async with ABH.conversation(event.chat_id, timeout=10) as conv:
            await conv.send_message("احسب")
            try:
                while True:
                    msg = await conv.get_response()
                    if msg.sender_id != target_user_id:
                        continue

                    text = msg.raw_text.strip()
                    match = re.search(r"([\d\s\+\-\*÷\/\.]+)\s*=", text)
                    if match:
                        expression = match.group(1).replace('÷', '/').replace('×', '*').strip()
                        try:
                            result = eval(expression)
                            if isinstance(result, float) and result.is_integer():
                                result = int(result)
                            await conv.send_message(str(result))
                        except Exception:
                            await conv.send_message("خطأ في الحساب.")
                    break
            except asyncio.TimeoutError:
                return
@ABH.on(events.NewMessage(pattern=r"^.جمل (\d+)$", outgoing=True))
async def words(event):
    await event.delete()
    num = int(event.pattern_match.group(1)) or 1
    for _ in range(num):
        async with ABH.conversation(event.chat_id, timeout=10) as conv:
            await conv.send_message("جمل")
            try:
                while True:
                    msg = await conv.get_response()
                    if msg.sender_id != target_user_id:
                        continue
                    text = msg.raw_text.strip()
                    match = re.search(r"\((.*?)\)", text)
                    if match:
                        inside = match.group(1)
                        cleaned = re.sub(r"[↢⇜'«»]", "", inside)
                        normalized = re.sub(r"\s+", " ", cleaned).strip()
                        await conv.send_message(normalized)
                    else:
                        return
                    break
            except asyncio.TimeoutError:
                return
