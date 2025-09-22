import os
import telebot

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "السلام عليكم 👋\nجاهز تبدأ تشتغل معانا وتعمل فلوس؟ 💰")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()

    # هنا تقدر تضيف الردود حسب الكلام اللي المستخدم هيكتبه بعد كده
    if "نعم" in text or "جاهز" in text:
        bot.reply_to(message, "تمام 😎، يلا نبدأ!")
    elif "لا" in text:
        bot.reply_to(message, "تمام، ممكن ترجع وقت ما تحب 👍")
    else:
        bot.reply_to(message, "مش فاهم قصدك 😅")

print("Bot is running...")
bot.infinity_polling()
