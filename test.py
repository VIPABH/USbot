import asyncio
from telethon import events, functions
from telethon.errors import RPCError, PasswordHashInvalidError

# استدعاء العميل الخاص بك
from ABH import ABH

CHANNEL_TO_TRANSFER = -1004303798955  # ايدي القناة
TARGET_USER = 7278066500               # ايدي المستلم
TWO_FA_PASSWORD = '11Onexvz3'         # كلمة السر

@ABH.on(events.NewMessage(outgoing=True, pattern=r'^(تيست|test)$'))
async def handle_test_command(event):
    reply_msg = await event.edit("⏳ جاري جلب البيانات وتنفيذ عملية نقل الملكية...")

    try:
        # 1. جلب الكيانات
        channel_entity = await ABH.get_entity(CHANNEL_TO_TRANSFER)
        user_entity = await ABH.get_entity(TARGET_USER)

        # 2. جلب وتشفير كلمة السر (2FA)
        pwd_check = await ABH.account.get_password()
        pwd_hash = ABH.compute_check_password(pwd_check, TWO_FA_PASSWORD)

        # 3. إرسال طلب نقل الملكية
        await ABH(functions.channels.EditCreatorRequest(
            channel=channel_entity,
            user_id=user_entity,
            password=pwd_hash
        ))

        await reply_msg.edit(
            f"✅ **تمت العملية بنجاح!**\n\n"
            f"📢 **القناة:** `{CHANNEL_TO_TRANSFER}`\n"
            f"👤 **المالك الجديد:** `{TARGET_USER}`"
        )

    except PasswordHashInvalidError:
        await reply_msg.edit("❌ **فشلت العملية:** كلمة السر (2FA) غير صحيحة.")
    except RPCError as e:
        await reply_msg.edit(f"❌ **خطأ من تليجرام (RPCError):** `{e.message}`")
    except Exception as e:
        await reply_msg.edit(f"❌ **حدث خطأ غير متوقع:**\n`{str(e)}`")
