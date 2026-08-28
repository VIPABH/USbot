import asyncio
import sqlite3
from datetime import datetime, timedelta
from telethon import events
from telethon.tl.functions.channels import (
    JoinChannelRequest,
    CreateChannelRequest,
    UpdateUsernameRequest
)
from telethon.errors import UserAlreadyParticipantError, FloodWaitError
from ABH import ABH

CHANNELS = ['x04ou', 'sszxl', 'sizxll', 'ANYMOUSupdate']
RETRY_INTERVAL = 300

hunt_task_handle = None
hunt_enabled = False
flood_until = None

def init_db():
    conn = sqlite3.connect('hunt_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hunt_users (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def set_hunt_user(user_id: int, username: str):
    conn = sqlite3.connect('hunt_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO hunt_users (user_id, username)
        VALUES (?, ?)
        ON CONFLICT(user_id) DO UPDATE SET username=excluded.username
    ''', (user_id, username))
    conn.commit()
    conn.close()

def get_hunt_user(user_id: int):
    conn = sqlite3.connect('hunt_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM hunt_users WHERE user_id = ?', (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def get_all_hunt_users():
    conn = sqlite3.connect('hunt_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT user_id, username FROM hunt_users')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_hunt_user(user_id: int):
    conn = sqlite3.connect('hunt_data.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM hunt_users WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()

init_db()

async def join_required_channels():
    for channel in CHANNELS:
        try:
            await ABH(JoinChannelRequest(channel))
        except UserAlreadyParticipantError:
            continue
        except Exception:
            pass

async def attempt_hunt(user_id: int, username: str):
    global flood_until
    
    username_clean = username.replace("@", "").strip()
    formatted_user = f"@{username_clean}"

    try:
        await ABH.get_entity(formatted_user)

    except ValueError:
        await ABH.send_message('me', f"🎯 اليوزر متاح حاليًا: {formatted_user}")
        try:
            result = await ABH(CreateChannelRequest(
                title="صيد اليوزرات 🚀",
                about="قناة تخزين اليوزرات المقتنصة تلقائيًا",
                megagroup=False
            ))
            new_channel = result.chats[0]
            
            await ABH(UpdateUsernameRequest(
                channel=new_channel,
                username=username_clean
            ))
            
            await ABH.send_message('me', f"📌 تم تثبيت المعرف بنجاح على قناة: {formatted_user}")
            delete_hunt_user(user_id)

        except FloodWaitError as err:
            flood_until = datetime.now() + timedelta(seconds=err.seconds)
            await ABH.send_message(
                'me',
                f"⚠️ تم تقييد الحساب (FloodWait) لمدة {err.seconds} ثانية.\n"
                f"⏳ يتوقف الصيد مؤقتًا حتى: {flood_until.strftime('%H:%M:%S')}"
            )

        except Exception as err:
            await ABH.send_message('me', f"⚠️ فشل تثبيت المعرف {formatted_user}\n{err}")

    except FloodWaitError as err:
        flood_until = datetime.now() + timedelta(seconds=err.seconds)

async def hunt_task() -> bool:
    users = get_all_hunt_users()
    if not users:
        return False

    await join_required_channels()

    for user_id, username in users:
        if flood_until and datetime.now() < flood_until:
            break
        if username:
            await attempt_hunt(user_id, username)
            
    return True

async def periodic_hunt():
    global hunt_task_handle, flood_until
    
    while hunt_enabled:
        if flood_until:
            now = datetime.now()
            if now < flood_until:
                wait_seconds = (flood_until - now).total_seconds()
                await asyncio.sleep(wait_seconds)
            flood_until = None

        has_users = await hunt_task()
        if has_users and not flood_until:
            await ABH.send_message('me', "🚀 تم تشغيل دورة فحص وصيد اليوزرات.")
            
        await asyncio.sleep(RETRY_INTERVAL)
        
    hunt_task_handle = None

@ABH.on(events.NewMessage(pattern=r"^(الصيد|حالة الصيد)$"))
async def shows(e):
    current_user = get_hunt_user(e.sender_id)
    user_display = current_user if current_user else "لا يوجد يوزر مخزن"

    status_display = "🟢 شغال (مفعل)" if hunt_enabled else "🔴 متوقف (معطل)"

    if flood_until and datetime.now() < flood_until:
        remaining = flood_until - datetime.now()
        hours, remainder = divmod(int(remaining.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        band_status = f"⚠️ مبند مؤقتًا\n⏳ باقي للباند: {hours:02d}:{minutes:02d}:{seconds:02d}"
    else:
        band_status = "✅ غير مبند (طبيعي)"

    now_str = datetime.now().strftime("%Y-%m-%d | %I:%M:%S %p")

    report = (
        f"📊 **تقرير حالة الصيد الشاملة**\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"⚙️ **حالة الصيد:** {status_display}\n"
        f"🎯 **اليوزر الحالي:** `{user_display}`\n"
        f"🛡️ **حالة الحساب:** {band_status}\n"
        f"⏰ **الوقت الحالي:** `{now_str}`\n"
        f"━━━━━━━━━━━━━━━━━━"
    )
    
    if e.out:
        await e.edit(report)
    else:
        await e.respond(report)

@ABH.on(events.NewMessage(pattern=r"^الصيد (تفعيل|تعطيل)$"))
async def toggle_hunt(e):
    global hunt_enabled, hunt_task_handle
    action = e.pattern_match.group(1)

    if action == "تفعيل":
        if hunt_enabled:
            text = "✅ الصيد مفعل بالفعل."
            return await e.edit(text) if e.out else await e.respond(text)
            
        hunt_enabled = True
        text = "🚀 تم تفعيل حلقة الصيد بنجاح."
        if e.out:
            await e.edit(text)
        else:
            await e.respond(text)
        
        if not hunt_task_handle:
            hunt_task_handle = ABH.loop.create_task(periodic_hunt())
    else:
        hunt_enabled = False
        text = "🛑 تم تعطيل حلقة الصيد."
        if e.out:
            await e.edit(text)
        else:
            await e.respond(text)

@ABH.on(events.NewMessage(pattern=r"^صيد (@?\w+)$"))
async def save(e):
    user = e.pattern_match.group(1)
    
    if not user.startswith('@'):
        user = f"@{user}"

    set_hunt_user(e.sender_id, user)
    text = f"✅ تم حفظ اليوزر بنجاح: `{user}`"
    
    if e.out:
        await e.edit(text)
    else:
        await e.respond(text)
