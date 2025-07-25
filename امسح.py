from ABH import ABH, events
from التخزين import *
# from config import vars
from telethon.tl.types import (
    InputMessagesFilterDocument,
    InputMessagesFilterPhotos,
    InputMessagesFilterUrl
)
# HVAR = vars("hidvar")
# GVAR = vars("gidvar")
@ABH.on(events.NewMessage(pattern="^.امسح$", outgoing=True))
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
            if message:
                sender = await message.get_sender()
                if sender and not sender.bot:
                    await message.delete()
                    deleted_counts[msg_type] += 1
                    total_deleted += 1
    # if total_deleted > 0:
    #     details = "\n".join([f"{msg_type}: {count}" for msg_type, count in deleted_counts.items() if count > 0])
    #     message_text = f"🗑️ تم حذف {total_deleted} رسالة.\n\n التفاصيل:\n{details}"
    # else:
    #     message_text = "لم يتم العثور على رسائل مطابقة للفلاتر المحددة."
    # try:
    #     await ABH.send_message(int(HVAR), message_text)
    # except Exception as e:
    #     print("Error:", e)
    #     print("HVAR:", HVAR)
    #     await ABH.send_message(event.chat_id, "حدث خطأ أثناء إرسال الرسالة إلى مجموعة الإشعارات.")
