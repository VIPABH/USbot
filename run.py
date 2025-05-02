from موارد import ABH
import UScode
import asyncio
async def main():
    await ABH.start()
    print("◉ البوت يعمل الآن")
    await ABH.run_until_disconnected()
asyncio.run(main())
