from telethon import events
from telethon.tl.functions.messages import ReportRequest
from telethon.tl.types import InputReportReasonSpam, InputReportReasonViolence, InputReportReasonPornography
from ABH import ABH

@ABH.on(events.NewMessage(pattern='بلاغ (.+)', outgoing=True))
async def report_handler(event):
    try:
        # احصل على الرسالة المرد عليها
        msg = await event.get_reply_message()
        if not msg:
            await event.reply("⚠️ الرجاء الرد على الرسالة التي تريد الإبلاغ عنها.")
            return

        # تحويل الـ chat_id إلى InputPeer صالح
        peer = await ABH.get_input_entity(msg.chat_id)

        # حدد سبب الإبلاغ
        reason = InputReportReasonPornography()  # يمكنك تغييره لأي سبب

        # إرسال البلاغ بدون keyword arguments
        result = await ABH(ReportRequest(
            peer,           # هنا InputPeer
            [msg.id],       # قائمة بالرسائل
            reason,         # سبب الإبلاغ
            "رسالة مزعجة"  # وصف optional
        ))

        await event.reply("✅ تم الإبلاغ عن الرسالة بنجاح.")

    except Exception as e:
        print(f"Error: {e}")
        await event.reply("❌ حدث خطأ أثناء معالجة البلاغ.")
