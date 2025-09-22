import os
import telebot

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

# قائمة الصور (ملفات محلية)
photos = ["apple1.jpg", "apple2.jpg", "apple3.jpg"]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "السلام عليكم 👋\nجاهز تبدأ تشتغل معانا وتعمل فلوس؟ 💰")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # الرسالة الثانية (بدون صور)
    second_msg = "كل يوم بنزل إشارات للعبة 🍎Apple Of Fortune🍎 اللي بتساعد الناس يكسبوا بشكل ثابت أكتر من 5000 جنيه في اليوم. الموضوع بسيط جدًا: أنا بقولك تراهن فين، إنت بتكرر، وإنت بتكسب."
    bot.send_message(message.chat.id, second_msg)

    # الرسالة الثالثة (مدموجة مع الصور)
    third_msg = """بص على نتايج عملائي 👆
الناس دي عمرها ما سمعت عن لعبة 🍎Apple Of Fortune🍎 قبل كده وماكانوش يعرفوا إن ممكن يكسبوا منها.
دلوقتي، بفضل إشاراتي، بيكسبوا 5000 جنيه في اليوم 💸
"""
    for photo_file in photos:
        with open(photo_file, "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption=third_msg)

print("Bot is running...")
bot.infinity_polling()
