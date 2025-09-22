import os
import telebot
from telebot.types import InputMediaPhoto

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

photos = ["apple1.jpg", "apple2.jpg", "apple3.jpg"]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "السلام عليكم 👋\nجاهز تبدأ تشتغل معانا وتعمل فلوس؟ 💰")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # الرسالة الثانية (بدون صور)
    second_msg = "كل يوم بنزل إشارات للعبة 🍎Apple Of Fortune🍎 اللي بتساعد الناس يكسبوا بشكل ثابت أكتر من 5000 جنيه في اليوم. الموضوع بسيط جدًا: أنا بقولك تراهن فين، إنت بتكرر، وإنت بتكسب."
    bot.send_message(message.chat.id, second_msg)

    # الرسالة الثالثة (صور + نص)
    third_msg = """بص على نتايج عملائي 👆
الناس دي عمرها ما سمعت عن لعبة 🍎Apple Of Fortune🍎 قبل كده وماكانوش يعرفوا إن ممكن يكسبوا منها.
دلوقتي، بفضل إشاراتي، بيكسبوا 5000 جنيه في اليوم 💸
"""

    media = []
    for i, photo_file in enumerate(photos):
        with open(photo_file, "rb") as photo:
            if i == 0:
                media.append(InputMediaPhoto(photo, caption=third_msg))
            else:
                media.append(InputMediaPhoto(photo))
    bot.send_media_group(message.chat.id, media)

print("Bot is running...")
bot.infinity_polling()
