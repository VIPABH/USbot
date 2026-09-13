import os
import json
import asyncio
from datetime import datetime
from telethon import events
from telethon.tl.functions.channels import CreateChannelRequest
from telethon.tl.functions.messages import CreateChatRequest

from ABH import ABH

SPECIAL_DATES = [
    (1, 1),  
    (2, 2),  
    (3, 3), 
    (4, 4),
    (5, 5),  
    (6, 6), 
    (7, 7), 
    (8, 8), 
    (9, 9), 
    (9, 13),
    (10, 10), 
    (11, 11), 
    (11, 28), 
    (12, 12),
    (12, 31), 
]

CHANNELS_COUNT = 5
GROUPS_COUNT = 5
JSON_FILE = "created_dates.json"

def load_created_dates():
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ خطأ أثناء قراءة ملف JSON: {e}")
        return []

def save_created_date(date_str):
    dates = load_created_dates()
    if date_str not in dates:
        dates.append(date_str)
        try:
            with open(JSON_FILE, "w", encoding="utf-8") as f:
                json.dump(dates, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"❌ خطأ أثناء حفظ التاريخ في ملف JSON: {e}")

async def create_special_channels_and_groups(current_day, current_month, date_str):
    title_base = f"{current_day}/{current_month}"
    
    try:
        await ABH.send_message('me', f"🎉 اليوم {title_base} يوم مميز! جاري البدء في إنشاء القنوات والمجموعات...")
    except Exception as e:
        print(f"❌ تعذر إرسال الإشعار: {e}")

    created_channels = 0
    for i in range(1, CHANNELS_COUNT + 1):
        channel_title = f"قناة {title_base} - {i}"
        try:
            await ABH(CreateChannelRequest(
                title=channel_title,
                about=f"قناة تلقائية تم إنشاؤها بتاريخ {title_base}",
                megagroup=False
            ))
            created_channels += 1
            await asyncio.sleep(2) 
        except Exception as e:
            print(f"❌ خطأ أثناء إنشاء القناة {channel_title}: {e}")

    created_groups = 0
    for i in range(1, GROUPS_COUNT + 1):
        group_title = f"مجموعة {title_base} - {i}"
        try:
            await ABH(CreateChatRequest(
                users=['me'],
                title=group_title
            ))
            created_groups += 1
            await asyncio.sleep(2)
        except Exception as e:
            print(f"❌ خطأ أثناء إنشاء المجموعة {group_title}: {e}")

    save_created_date(date_str)

    try:
        await ABH.send_message(
            'me',
            f"✅ **تم الانتهاء بنجاح!**\n\n"
            f"📢 تم إنشاء **{created_channels}** قناة.\n"
            f"👥 تم إنشاء **{created_groups}** مجموعة.\n"
            f"📁 تم حفظ التاريخ `{date_str}` في ملف JSON لمنع التكرار."
        )
    except Exception as e:
        print(f"❌ تعذر إرسال إشعار الأكتمال: {e}")

@ABH.on(events.NewMessage(outgoing=True))
async def check_on_outgoing_message(event):
    now = datetime.now()
    current_day = now.day
    current_month = now.month
    today_tuple = (current_day, current_month)

    if today_tuple not in SPECIAL_DATES:
        return

    date_str = f"{current_day}/{current_month}/{now.year}"
    created_dates = load_created_dates()

    if date_str in created_dates:
        return
    print("تم استلام الحدث")
    await create_special_channels_and_groups(current_day, current_month, date_str)
