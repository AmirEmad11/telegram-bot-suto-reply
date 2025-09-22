import asyncio
from telethon import TelegramClient, events, types
import os

# متغيرات البيئة
api_id = int(os.environ.get("api_id"))
api_hash = os.environ.get("api_hash")
phone = os.environ.get("phone")

channel_username = '@appleman112'  # ضع @appleman112 القناة العامة

client = TelegramClient('session_session', api_id, api_hash)

# الرسائل
welcome_msg = "السلام عليكم 👋\nجاهز تبدأ تشتغل معانا وتعمل فلوس؟ 💰"

second_msg = "كل يوم بنزل إشارات للعبة 🍎Apple Of Fortune🍎 اللي بتساعد الناس يكسبوا بشكل ثابت أكتر من 5000 جنيه في اليوم. الموضوع بسيط جدًا: أنا بقولك تراهن فين، إنت بتكرر، وإنت بتكسب."

third_msg = """بص على نتايج عملائي 👆
الناس دي عمرها ما سمعت عن لعبة 🍎Apple Of Fortune🍎 قبل كده وماكانوش يعرفوا إن ممكن يكسبوا منها.
دلوقتي، بفضل إشاراتي، بيكسبوا 5000 جنيه في اليوم 💸
"""

fourth_msg = """القواعد سهلة ✅

في الأول لازم تسجّل في الموقع بحساب جديد بالبرومو كود او الرمز الترويجي الخاص بينا New10

بعدها بتحط إيداع 190 جنيه، وبعدها بتستعمل إشاراتي الـ VIP عشان تكسب!

🚀 تابع قناتي وشوف بنفسك! 👇
https://t.me/+4HV7r58imh8yNGQ8

نصيبي هو 10% من أرباحك في الشهر!
خلينا نكون صريحين مع بعض 🤝😉
"""

photos = ["apple1.jpg", "apple2.jpg", "apple3.jpg"]
users_sent = set()
users_welcomed = set()

async def send_remaining_messages(user_id):
    if user_id not in users_sent:
        try:
            await client.send_message(user_id, second_msg)
            await asyncio.sleep(3)

            media = []
            for i, photo_file in enumerate(photos):
                if i == 0:
                    media.append(types.InputMediaPhoto(file=photo_file, caption=third_msg))
                else:
                    media.append(types.InputMediaPhoto(file=photo_file))
            try:
                await client.send_file(user_id, media)
            except Exception as e:
                print(f"Error sending photos: {e}")

            await asyncio.sleep(3)
            await client.send_message(user_id, fourth_msg)
        except Exception as e:
            print(f"Error sending messages: {e}")
        users_sent.add(user_id)

@client.on(events.ChatAction(chats=channel_username, user_added=True))
async def new_member(event):
    try:
        user = await event.get_user()
        if user.id not in users_welcomed:
            await client.send_message(user.id, welcome_msg)
            users_welcomed.add(user.id)
    except Exception as e:
        print(f"Error welcoming user: {e}")

@client.on(events.NewMessage)
async def handle_message(event):
    user_id = event.sender_id
    if user_id in users_welcomed and user_id not in users_sent:
        await send_remaining_messages(user_id)

async def main():
    await client.start(phone)
    print("Userbot running...")
    await client.run_until_disconnected()

asyncio.run(main())
