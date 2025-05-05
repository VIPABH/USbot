from ABH import ABH, ok, events #type:ignore
import asyncio
@ok
@ABH.on(events.NewMessage(pattern='^ها$', outgoing=True))
async def meme(event):
    await event.delete()
    r = await event.get_reply_message()
    if not r:
        return
    url = f"https://t.me/vipabh/1115"
    await ABH.send_file(r.id, url, caption="**Meme**", reply_to=r.id)
print('meme is running')
