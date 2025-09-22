import os
import telebot
from telebot.types import InputMediaPhoto

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

photos = ["apple1.jpg", "apple2.jpg", "apple3.jpg"]
users_sent = set()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "السلام عليكم 👋\nجاهز تبدأ تشتغل معانا وتعمل فلوس؟ 💰")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id

    if user_id not in users_sent:
        # الرسالة الثانية (نص بدون صور)
        second_msg = "كل يوم بنزل إشارات للعبة 🍎Apple Of Fortune🍎 اللي بتساعد الناس يكسبوا بشكل ثابت أكتر من 5000 جنيه في اليوم. الموضوع بسيط جدًا: أنا بقولك تراهن فين، إنت بتكرر، وإنت بتكسب."
        bot.send_message(user_id, second_msg)

        # الرسالة الثالثة (صور + نص)
        third_msg = """بص على نتايج عملائي 👆
الناس دي عمرها ما سمعت عن لعبة 🍎Apple Of Fortune🍎 قبل كده وماكانوش يعرفوا إن ممكن يكسبوا منها.
دلوقتي، بفضل إشاراتي، بيكسبوا 5000 جنيه في اليوم 💸
"""
        media = []
        for i, photo_file in enumerate(photos):
            photo = open(photo_file, "rb")
            if i == 0:
                media.append(InputMediaPhoto(photo, caption=third_msg))
            else:
                media.append(InputMediaPhoto(photo))
        bot.send_media_group(user_id, media)
        for m in media:
            m.media.close()

        # الرسالة الرابعة (القواعد)
        fourth_msg = """القواعد سهلة ✅

في الأول لازم تسجّل في الموقع بحساب جديد بالبرومو كود او الرمز الترويجي الخاص بينا New10

بعدها بتحط إيداع 190 جنيه، وبعدها بتستعمل إشاراتي الـ VIP عشان تكسب!

🚀 تابع قناتي وشوف بنفسك! 👇
https://t.me/+4HV7r58imh8yNGQ8

نصيبي هو 10% من أرباحك في الشهر!
خلينا نكون صريحين مع بعض 🤝😉
"""
        bot.send_message(user_id, fourth_msg)

        users_sent.add(user_id)

print("Bot is running...")
bot.infinity_polling()
