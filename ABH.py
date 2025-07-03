from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio, os, json
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
session_string = None
ABH = TelegramClient(StringSession(session_string), api_id, api_hash)
@ABH.on(events.NewMessage(pattern="^كود الجلسة", outgoing=True))
async def testup(event):
    global session_string
    session_string = ABH.session.save()
    await ABH.send_message('me', f"Session String:\n`{session_string}`")
def LOADVARS():
    config_file = "var.json"
    if os.path.exists(config_file):
        with open(config_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            gidvar = data.get("gidvar")
            hidvar = data.get("hidvar")
            return gidvar, hidvar
    return None, None
gidvar, hidvar = LOADVARS()
