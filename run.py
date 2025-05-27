import os
import sys
import asyncio
from telethon import events
from UScode import *
from config import *
from التخزين import *
from الردود import *
from امسح import *
from ذاتية import *
from ميمز import *
from ABH import *
from وعد import *


async def run_cmd(command: str):
    """تشغيل أمر في الشيل بشكل غير متزامن وانتظار نهايته"""
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return stdout.decode().strip(), stderr.decode().strip(), process.returncode

@ABH.on(events.NewMessage(pattern="^تحديث$", outgoing=True))
async def update_repo(event):
    msg = await event.edit("⏳ جاري جلب آخر التحديثات من الريبو عبر git pull ...")
    stdout, stderr, code = await run_cmd("git pull")
    if code == 0:
        await msg.edit(f"✅ تحديث السورس بنجاح:\n\n{stdout}\n\n"
                       f"⚠️ يرجى إعادة تشغيل البوت يدويًا أو انتظر إعادة التشغيل التلقائية.")
    else:
        await msg.edit(f"❌ حدث خطأ أثناء التحديث:\n\n{stderr}")

async def main():
    await ABH.start()
    print("البوت شغال الآن")
    await ABH.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
