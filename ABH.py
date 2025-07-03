from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio, os, json
api_id = int(os.getenv("API_ID") or input("📌 أدخل api_id: "))
api_hash = os.getenv("API_HASH") or input("📌 أدخل api_hash: ")
SESSION_FILE = "session.txt"
if os.path.exists(SESSION_FILE):
    with open(SESSION_FILE, "r") as f:
        session_str = f.read().strip()
        print("✅ تم العثور على جلسة محفوظة")
else:
    session_str = None
    print("⚠️ لا توجد جلسة محفوظة، سيتم إنشاء جلسة جديدة")
ABH = TelegramClient(StringSession(session_str), api_id, api_hash)
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
