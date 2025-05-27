from datetime import datetime
from telethon import events
from ABH import ABH
import os, sys
now = datetime.now()
تاريخ = now.strftime("%Y-%m-%d")
ساعة = now.strftime("%I:%M:%S %p")
@ABH.on(events.NewMessage(pattern="^.فحص|فحص؟", outgoing=True))
async def testup(event):
    now = datetime.now()
    التاريخ = now.strftime("%Y-%m-%d")
    السااعة = now.strftime("%I:%M:%S %p")
    start = datetime.now()
    await event.edit("**᯽︙ جـاري فـحص الـبـوت**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    cap = (
        f"**᯽︙ السورس شغال**\n"
        f"᯽︙ **الـتـاريخ:** `{التاريخ}`\n"
        f"᯽︙ **الـسـاعه:** `{السااعة}`\n"
        f"᯽︙ **الـزمن:** `{ms} ms`\n"
        f"᯽︙ **الـبـوت شغال 100%**"
    )
    await event.delete()
    pic = 'https://files.catbox.moe/ebn0d8.jpg'
    await event.respond(file=pic, message=cap)
async def run_cmd(command: str):
    """تشغيل أمر في الشيل بشكل غير متزامن وانتظار نهايته"""
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return stdout.decode().strip(), stderr.decode().strip(), process.returncode
@ABH.on(events.NewMessage(pattern="^اعادة تشغيل$", outgoing=True))
async def restart_bot(event):
    msg = await event.respond(" جاري جلب آخر التحديثات من الريبو عبر ...")
    stdout, stderr, code = await run_cmd("git pull")
    if code == 0:
        await msg.edit(f"تحديث السورس بنجاح:\n\n{stdout}\n\n جاري إعادة تشغيل البوت...")
        await client.disconnect()
        os.execv(sys.executable, [sys.executable] + sys.argv)
    else:
        await msg.edit(f"حدث خطأ أثناء التحديث:\n\n{stderr}")
