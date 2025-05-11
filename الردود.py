import json
import os
from ABH import *
from telethon import events

FILE_PATH = "ردود.json"

def load_data():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_response(chat_id, keyword, resp_type, content):
    data = load_data()
    cid = str(chat_id)
    if cid not in data:
        data[cid] = {}
    data[cid][keyword] = {
        "type": resp_type,
        "data": content
    }
    save_data(data)

def get_response(chat_id, keyword):
    data = load_data()
    return data.get(str(chat_id), {}).get(keyword)

@ABH.on(events.NewMessage(pattern=r'^\.اضف_رد\s+(\S+)$', outgoing=True))
async def add_reply(event):
    reply = await event.get_reply_message()
    if not reply:
        return await event.reply("❌ يجب الرد على رسالة تحتوي على رد.")

    keyword = event.pattern_match.group(1).strip()
    chat_id = event.chat_id

    if reply.media and reply.file:
        # تحميل الملف إلى السيرفر وحفظه في المجلد الحالي
        path = await reply.download_media(file="files/")
        file_info = {
            "file_path": path,  # حفظ المسار المحلي للملف
            "name": reply.file.name or "file"
        }
        add_response(chat_id, keyword, "file", file_info)
        await event.reply(f"✅ تم حفظ الملف كـ رد للكلمة: `{keyword}`")
    elif reply.text:
        add_response(chat_id, keyword, "text", reply.text.strip())
        await event.reply(f"✅ تم حفظ النص كـ رد للكلمة: `{keyword}`")
    else:
        await event.reply("❌ الرد لا يحتوي على نص أو وسائط.")

@ABH.on(events.NewMessage(pattern=r'^رد\s+(\S+)$', outgoing=True))
async def add_reply_alias(event):
    await add_reply(event)  # إعادة استخدام نفس الدالة

@ABH.on(events.NewMessage())
async def auto_reply(event):
    text = event.raw_text.strip()
    if not text:
        return
    chat_id = event.chat_id
    reply_data = get_response(chat_id, text)
    if not reply_data:
        return

    if reply_data["type"] == "text":
        await event.reply(reply_data["data"])
    elif reply_data["type"] == "file":
        try:
            # إرسال الملف المحفوظ من المسار المحلي
            await ABH.send_file(
                event.chat_id,
                file=reply_data["data"]["file_path"],
                caption=f"📎 {reply_data['data'].get('name', '')}"
            )
        except Exception as e:
            await event.reply(f"⚠️ تعذر إرسال الملف. السبب: {e}")
