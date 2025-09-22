import os
import telebot

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "السلام عليكم 👋\nجاهز تبدأ تشتغل معانا وتعمل فلوس؟ 💰")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "كل يوم بنزل إشارات للعبة 🍎Apple Of Fortune🍎 اللي بتساعد الناس يكسبوا بشكل ثابت أكتر من 5000 جنيه في اليوم. الموضوع بسيط جدًا: أنا بقولك تراهن فين، إنت بتكرر، وإنت بتكسب.")

print("Bot is running...")
bot.infinity_polling()
