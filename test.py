import asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.channels import EditCreatorRequest
from telethon.errors import (
    PasswordHashInvalidError, 
    ChannelsAdminPublicRequiredError, 
    TwoFactorRequiredError,
    ChannelInvalidError
)

# ==========================================
CHANNEL_TO_TRANSFER = -1004303798955  # رابط/معرف القناة
TARGET_USER = 7278066500           # معرف الشخص المستلم
TWO_FA_PASSWORD = '11Onexvz3'     # كلمة سر التحقق بخطوتين الخاص بملكيتك

@ABH.on(events.NewMessage(outgoing=True, pattern=r'^(تيست|test)$'))
async def handle_test_command(event):
    """
    عند إرسال أمر 'تيست' من الحساب نفسه، سيتم تنفيذ النقل والرد بالتفاصيل.
    """
    # تعديل الرسالة لتوضيح بدء العملية
    reply_msg = await event.edit("⏳ جاري جلب البيانات وتنفيذ عملية نقل الملكية...")

    try:
        # 1. جلب الكيانات
        channel_entity = await ABH.get_entity(CHANNEL_TO_TRANSFER)
        user_entity = await ABH.get_entity(TARGET_USER)

        # 2. التشفير والتحقق من كلمة السر
        pwd_check = await ABH.account.get_password()
        pwd_hash = ABH.compute_check_password(pwd_check, TWO_FA_PASSWORD)

        # 3. إرسال طلب نقل الملكية
        await ABH(EditCreatorRequest(
            channel=channel_entity,
            user_id=user_entity,
            password=pwd_hash
        ))

        # رسالة النجاح
        await reply_msg.edit(
            f"✅ **تمت العملية بنجاح!**\n\n"
            f"📢 **القناة:** {CHANNEL_TO_TRANSFER}\n"
            f"👤 **المالك الجديد:** {TARGET_USER}"
        )

    except PasswordHashInvalidError:
        await reply_msg.edit("❌ **فشلت العملية:** كلمة السر (2FA) غير صحيحة.")
    except TwoFactorRequiredError:
        await reply_msg.edit("❌ **فشلت العملية:** التحقق بخطوتين غير مفعل بالحساب.")
    except ChannelsAdminPublicRequiredError:
        await reply_msg.edit("❌ **فشلت العملية:** لا تملك صلاحيات كافية لنقل القناة.")
    except ChannelInvalidError:
        await reply_msg.edit("❌ **فشلت العملية:** اسم القناة غير صحيح أو غير موجود.")
    except Exception as e:
        await reply_msg.edit(f"❌ **حدث خطأ غير متوقع:**\n`{str(e)}`")

print("البوت يعمل الآن.. أرسل كلمة (تيست) من الحساب لتشغيل الأمر.")
