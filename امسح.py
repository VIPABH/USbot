from ABH import ABH, events, ok #type: ignore
from التخزين import hidvar #type: ignore
from telethon.tl.types import (
    InputMessagesFilterDocument,
    InputMessagesFilterPhotos,
    InputMessagesFilterUrl
)
@ok
@ABH.on(events.NewMessage(pattern="^.امسح$"))
async def delete_all(event):
    await event.delete()
    filters = {
        "الملفات": InputMessagesFilterDocument,
        "الروابط": InputMessagesFilterUrl,
        "الصور": InputMessagesFilterPhotos
        }
    total_deleted = 0
    deleted_counts = {key: 0 for key in filters.keys()}
    for msg_type, msg_filter in filters.items():
        async for message in event.client.iter_messages(event.chat_id, filter=msg_filter):
                excluded_user_ids = [793977288, 1421907917, 7308514832, 6387632922, 7908156943]
                if message.sender_id in excluded_user_ids:
                    continue 
                if message:
                    await message.delete()
                    deleted_counts[msg_type] += 1
                    total_deleted += 1
        if total_deleted > 0:
            details = "\n".join([f"{msg_type}: {count}" for msg_type, count in deleted_counts.items() if count > 0])
            await ABH.send_message(hidvar, f"تم حذف {total_deleted} رسالة.\nالتفاصيل:\n{details}")
        else:
            await ABH.send_message(int(hidvar), "لا توجد رسائل تطابق الفلاتر المحددة!")
