import asyncio
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
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
    (10, 10), 
    (11, 11), 
    (11, 28), 
    (12, 12),
    (12, 31), 
]

CHANNELS_COUNT = 5
GROUPS_COUNT = 5
ME_USERNAME = 'me'
async def check_and_create_special():
    now = datetime.now()
    current_day = now.day
    current_month = now.month
    if (current_day, current_month) in SPECIAL_DATES:
        title_base = f"{current_day}/{current_month}"
        try:
            await ABH.send_message("me", f"🎉 اليوم {title_base} يوم مميز! جاري البدء في إنشاء القنوات والمجموعات...")
        except Exception as e:
            print(f"❌ تعذر إرسال الإشعار: {e}")
        for i in range(1, CHANNELS_COUNT + 1):
            channel_title = f"قناة {title_base} - {i}"
            try:
                await ABH(CreateChannelRequest(
                    title=channel_title,
                    about=f"قناة تلقائية تم إنشاؤها بتاريخ {title_base}",
                    megagroup=False
                ))
                print(f"✅ تم إنشاء: {channel_title}")
                await asyncio.sleep(2) 
            except Exception as e:
                print(f"❌ خطأ أثناء إنشاء القناة {channel_title}: {e}")
        for i in range(1, GROUPS_COUNT + 1):
            group_title = f"مجموعة {title_base} - {i}"
            try:
                await ABH(CreateChatRequest(
                    users=[ME_USERNAME],
                    title=group_title
                ))
                print(f"✅ تم إنشاء: {group_title}")
                await asyncio.sleep(2)
            except Exception as e:
                print(f"❌ خطأ أثناء إنشاء المجموعة {group_title}: {e}")
    else:
        print(f"ℹ️ اليوم {current_day}/{current_month} ليس ضمن الأيام المميزة.")

def setup_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_and_create_special, 'cron', hour=0, minute=0)
    scheduler.start()
setup_scheduler()
