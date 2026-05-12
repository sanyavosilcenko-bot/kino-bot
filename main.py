import os
from flask import Flask
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# ===== TOKEN =====
TOKEN = os.getenv("8765560176:AAEk6ndHtYD7NgFCubFUJHSjTolFwmaR7qA")

# ===== MAJBURIY OBUNA KANALI =====
CHANNEL = "@kinolaruztvv"   # BU YERGA KANAL USERNAME YOZING

# ===== OBUNA TEKSHIRISH =====
def check_sub(update, context):
    user_id = update.effective_user.id

    try:
        member = context.bot.get_chat_member(CHANNEL, user_id)

        if member.status in ["member", "administrator", "creator"]:
            return True
        else:
            update.message.reply_text(
                f"❌ Botdan foydalanish uchun kanalga obuna bo‘ling:\n"
                f"https://t.me/{CHANNEL.replace('@','')}"
            )
            return False
    except:
        update.message.reply_text("⚠️ Kanal topilmadi yoki bot admin emas")
        return False

# ===== START =====
def start(update, context):
    if not check_sub(update, context):
        return

    update.message.reply_text(
        "🎬 Kino botga xush kelibsiz!\n\nKino nomini yozing."
    )

# ===== KINO BAZA =====
movies = {
    "avatar": "🎬 Avatar (2009)\n👉 https://t.me/example_movie1",
    "spiderman": "🎬 Spider-Man\n👉 https://t.me/example_movie2",
    "fast": "🎬 Fast & Furious\n👉 https://t.me/example_movie3",
}

# ===== KINO QIDIRISH =====
def search_movie(update, context):
    if not check_sub(update, context):
        return

    text = update.message.text.lower()

    if text in movies:
        update.message.reply_text(movies[text])
    else:
        update.message.reply_text("❌ Kino topilmadi")

# ===== TELEGRAM BOT =====
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, search_movie))

# ===== RENDER SERVER =====
app = Flask(__name__)

@app.route("/")
def home():
    return "Kino bot ishlayapti ✅"

# ===== RUN =====
if __name__ == "__main__":
    updater.start_polling()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
