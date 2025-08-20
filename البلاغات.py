from telethon import events
from telethon.tl.functions.messages import ReportRequest
from telethon.tl.types import InputReportReasonSpam
from ABH import ABH

@ABH.on(events.NewMessage(pattern='بلاغ', outgoing=True))
async def report_handler(event):
    try:
        msg = await event.get_reply_message()
        if not msg:
            await event.reply("⚠️ الرجاء الرد على الرسالة التي تريد الإبلاغ عنها.")
            return

        peer = await ABH.get_input_entity(msg.chat_id)

        # إرسال البلاغ كـ spam
        await ABH(ReportRequest(
            peer=peer,
            id=[msg.id],
            reason=InputReportReasonSpam(),  # فقط Spam يعمل حالياً
            message="رسالة مزعجة"
        ))

        await event.reply("✅ تم الإبلاغ عن الرسالة بنجاح.")

    except Exception as e:
        print(f"Error: {e}")
        await event.reply("❌ حدث خطأ أثناء معالجة البلاغ.")
