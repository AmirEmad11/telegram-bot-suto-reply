import os
import telebot
from telebot.types import InputMediaPhoto
import time

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

photos = ["apple1.jpg", "apple2.jpg", "apple3.jpg"]
users_sent = set()        # المستخدمين اللي استلموا باقي الرسائل
users_welcomed = set()    # المستخدمين اللي استلموا الترحيب

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

# دالة لإرسال باقي الرسائل بعد الترحيب
def send_remaining_messages(user_id):
    if user_id not in users_sent:
        bot.send_message(user_id, second_msg)
        time.sleep(3)

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
        time.sleep(3)

        bot.send_message(user_id, fourth_msg)
        users_sent.add(user_id)

# إرسال الترحيب فورًا عند /start
@bot.message_handler(commands=['start'])
def start_command(message):
    user_id = message.chat.id
    if user_id not in users_welcomed:
        bot.send_message(user_id, welcome_msg)
        users_welcomed.add(user_id)

# متابعة أي رسالة بعد الترحيب لإرسال باقي الرسائل
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id
    if user_id in users_welcomed and user_id not in users_sent:
        send_remaining_messages(user_id)
    # بعد كده لا يرسل أي رد تلقائي، المستخدم يقدر يتكلم بحرية

# مراقبة انضمام المستخدمين للقناة (Supergroup أو linked group)
@bot.chat_member_handler()
def handle_new_member(chat_member_update):
    new_status = chat_member_update.new_chat_member.status
    user = chat_member_update.new_chat_member.user
    if new_status == "member" and user.id not in users_welcomed:
        try:
            bot.send_message(user.id, welcome_msg)
            users_welcomed.add(user.id)
        except Exception as e:
            print(f"مشكلة في ارسال الترحيب للعضو {user.id}: {e}")

print("Bot is running...")
bot.infinity_polling()
