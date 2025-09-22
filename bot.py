import asyncio
from telethon import TelegramClient, events, types

# بيانات حسابك الشخصي
api_id = 21943267
api_hash = 'd120be656f0dbe54a4ed369e70c2319b'
phone = '+201014367365'

# اسم القناة
channel_username = '@appleman112'

client = TelegramClient('session', api_id, api_hash)

welcome_msg = "السلام عليكم 👋\nجاهز تبدأ تشتغل معانا وتعمل فلوس؟ 💰"

@client.on(events.ChatAction(chats=channel_username, user_added=True))
async def new_member(event):
    try:
        user = await event.get_user()
        # إرسال رسالة الترحيب مباشرة بعد الانضمام
        await client.send_message(user.id, welcome_msg)
        print(f"تم الترحيب بالعضو {user.id}")
    except Exception as e:
        print(f"Error: {e}")

async def main():
    await client.start(phone)
    print("Userbot running...")
    await client.run_until_disconnected()

asyncio.run(main())
