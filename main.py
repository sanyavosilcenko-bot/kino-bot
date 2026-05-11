from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "8765560176:AAEk6ndHtYD7NgFCubFUJHSjTolFwmaR7qA"
CHANNEL = "@kinolaruztvv"   # shu yerga o'zingni kanal yozasan

# 🔍 Kanalga obuna tekshirish
def check_subscriber(bot, user_id):
    try:
        member = bot.get_chat_member(CHANNEL, user_id)
        if member.status in ["member", "administrator", "creator"]:
            return True
        return False
    except:
        return False

# 🚀 START BUYRUQ
def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id

    if check_subscriber(context.bot, user_id):

        update.message.reply_text(
            "🎬 Xush kelibsiz!\nKino botga hush kelibsiz.\n\nFilmni tanlang:"
        )

        # oddiy kino menu
        keyboard = [
            [InlineKeyboardButton("🎥 Kino 1", callback_data='kino1')],
            [InlineKeyboardButton("🎥 Kino 2", callback_data='kino2')],
        ]

        update.message.reply_text(
            "👇 Tanlang:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    else:
        # ❌ obuna bo'lmagan
        keyboard = [
            [InlineKeyboardButton("📢 Kanalga obuna bo'lish", url=f"https://t.me/{CHANNEL.replace('@','')}")],
            [InlineKeyboardButton("🔄 Tekshirish", callback_data='check')]
        ]

        update.message.reply_text(
            "❗ Botdan foydalanish uchun kanalga obuna bo'ling!",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

# 🔄 callback (tugmalar)
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id

    if query.data == "check":
        if check_subscriber(context.bot, user_id):
            query.edit_message_text("✅ Rahmat! Siz obuna bo'lgansiz. /start bosing")
        else:
            query.edit_message_text("❌ Hali ham obuna emassiz!")

    elif query.data == "kino1":
        query.edit_message_text("🎥 Kino 1: https://example.com/movie1")

    elif query.data == "kino2":
        query.edit_message_text("🎥 Kino 2: https://example.com/movie2")

# ▶️ BOT ISHLATISH
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(telegram.ext.CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
