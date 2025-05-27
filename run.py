from telethon import events
import asyncio, os, sys
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
async def reconnect_client(client):
    """دالة لإعادة تشغيل الاتصال بالبوت"""
    await client.disconnect()
    await client.start()
@ABH.on(events.NewMessage(pattern="^اعادة تشغيل$", outgoing=True))
async def restart_bot(event):
    msg = await event.edit(" جاري جلب آخر التحديثات من الريبو عبر git pull ...")
    stdout, stderr, code = await run_cmd("git pull")
    if code == 0:
        await msg.edit(f"تحديث السورس بنجاح:\n\n{stdout}\n\n🔄 جاري إعادة الاتصال بالبوت...")
        await reconnect_client(ABH)
        await msg.edit(" تم إعادة الاتصال بالبوت بنجاح بعد التحديث.")
        await client.start()
    else:
        await msg.edit(f" حدث خطأ أثناء التحديث:\n\n{stderr}")
async def main():
    await ABH.start()
    print("run is running")
    await config_vars()
    await ABH.run_until_disconnected()
asyncio.run(main())
