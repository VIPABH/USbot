from telethon.tl.functions.messages import ReportRequest
from telethon.tl.types import InputReportReasonSpam
from telethon.tl.types import (
    InputReportReasonSpam,
    InputReportReasonViolence,
    InputReportReasonPornography
)
reason = InputReportReasonSpam()
reason = InputReportReasonViolence()
reason = InputReportReasonPornography()
from telethon import events
from ABH import ABH
@ABH.on(events.NewMessage(pattern='بلاغ (.+) ', outgoing=True))
async def report_handler(event):
    try:
        reason = event.pattern_match.group(1).strip().lower()
        if reason == "مزعج":
            reason = InputReportReasonSpam()
        elif reason == "عنف":
            reason = InputReportReasonViolence()
        elif reason == "إباحية":
            reason = InputReportReasonPornography()
        else:
            await event.reply("السبب غير معروف. يرجى استخدام 'مزعج' أو 'عنف' أو 'إباحية'.")
            return
        msg_id = await event.get_reply_message()
        print(msg_id)
        result = await ABH(ReportRequest(
            peer=msg_id.chat_id,
            id=[msg_id.id],
            reason=InputReportReasonSpam(),
            message="رسالة مزعجة"
        ))
        if result:
            await event.reply("تم الإبلاغ عن الرسالة بنجاح.")
        else:
            await event.reply("فشل الإبلاغ عن الرسالة.")
    except Exception as e:
        print(f"Error: {e}")
        await event.reply("حدث خطأ أثناء معالجة البلاغ.")
