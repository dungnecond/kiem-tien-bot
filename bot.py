from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 Kiếm tiền online", callback_data="kiem_tien")],
        [InlineKeyboardButton("📚 Hướng dẫn", callback_data="huong_dan")],
        [InlineKeyboardButton("📞 Liên hệ", callback_data="lien_he")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🤖 BOT KIẾM TIỀN ONLINE\n\nChọn mục bên dưới 👇",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "kiem_tien":
        await query.edit_message_text(
            "💸 CÁCH KIẾM TIỀN ONLINE:\n\n"
            "1️⃣ Tiếp thị liên kết\n"
            "2️⃣ Làm nhiệm vụ online\n"
            "3️⃣ Bán tài khoản số\n"
            "4️⃣ Rút gọn link kiếm tiền"
        )

    elif query.data == "huong_dan":
        await query.edit_message_text(
            "📚 HƯỚNG DẪN:\n"
            "- Không cần vốn\n"
            "- Làm bằng điện thoại\n"
            "- Phù hợp học sinh – sinh viên"
        )

    elif query.data == "lien_he":
        await query.edit_message_text(
            "📞 LIÊN HỆ ADMIN:\n"
            "Telegram: @yourusername"
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("Bot dang chay...")
app.run_polling()
