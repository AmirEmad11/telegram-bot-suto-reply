import asyncio
from telethon import TelegramClient, events
import os

# متغيرات البيئة
api_id = int(os.environ.get("api_id"))
api_hash = os.environ.get("api_hash")
phone = os.environ.get("phone")

# ضع @username القناة العامة بالضبط
channel_username = '@MyBroadcastChannel'

client = TelegramClient('session_session', api_id, api_hash)

# رسالة الترحيب التجريبية
welcome_msg = "السلام عليكم 👋\nجاهز تبدأ تشتغل معانا وتعمل فلوس؟ 💰"

@client.on(events.ChatAction(chats=channel_username, user_added=True))
async def new_member(event):
    try:
        user = await event.get_user()
        await client.send_message(user.id, welcome_msg)
        print(f"تم ارسال الترحيب لـ {user.id}")
    except Exception as e:
        print(f"Error welcoming user: {e}")

async def main():
    await client.start(phone)
    print("Userbot running...")
    await client.run_until_disconnected()

asyncio.run(main())
