from telethon import events
from telethon.tl.functions.messages import ReportRequest
from telethon.tl.types import (
    InputReportReasonSpam,
    InputReportReasonViolence,
    InputReportReasonPornography
)
from ABH import ABH
@ABH.on(events.NewMessage(pattern='بلاغ (.+)', outgoing=True))
async def report_handler(event):
    try:
        # reason_text = event.pattern_match.group(1).strip()
        # if reason_text == "مزعج":
        #     reason = InputReportReasonSpam()
        # elif reason_text == "عنف":
        #     reason = InputReportReasonViolence()
        # elif reason_text == "إباحية":
        #     reason = InputReportReasonPornography()
        # else:
        #     await event.reply("⚠️ السبب غير معروف. استخدم: 'مزعج' أو 'عنف' أو 'إباحية'.")
        #     return
        msg = await event.get_reply_message()
        if not msg:
            await event.reply("⚠️ الرجاء الرد على الرسالة التي تريد الإبلاغ عنها.")
            return
        result = await ABH(ReportRequest(
            peer=event.chat_id,
            id=[msg.id],
            reason=InputReportReasonPornography(),
            message="رسالة مزعجة"
        ))
        if result:
            await event.reply("✅ تم الإبلاغ عن الرسالة بنجاح.")
        else:
            await event.reply("❌ فشل الإبلاغ عن الرسالة.")
    except Exception as e:
        print(f"Error: {e}")
        await event.reply("❌ حدث خطأ أثناء معالجة البلاغ.")
