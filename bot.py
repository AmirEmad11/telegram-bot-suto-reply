from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os

# التوكن هيتسحب من Environment Variables (هتحطه في Render بعدين)
TOKEN = os.getenv("TOKEN")

# متغير يحدد إذا كانت دي أول رسالة من اليوزر ولا لأ
user_first_message = {}

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    if user_id not in user_first_message:
        user_first_message[user_id] = True
        await update.message.reply_text("👋 أهلاً بيك! دي أول رسالة ليك معانا ❤️")
    else:
        await update.message.reply_text("✅ شكرًا لرسالتك، هنرد عليك قريب.")

# إعداد البوت
app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

if __name__ == "__main__":
    app.run_polling()
