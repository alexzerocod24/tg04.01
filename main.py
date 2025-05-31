from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

API_TOKEN = '7803175828:AAH73o1QVOZ3f_kHk0M-ICKWZ0luYXq0GhU'

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Привет"), KeyboardButton("Пока")]
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Выберите действие:", reply_markup=keyboard)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_name = update.message.from_user.first_name or "пользователь"

    if text == "Привет":
        await update.message.reply_text(f"Привет, {user_name}!")
    elif text == "Пока":
        await update.message.reply_text(f"До свидания, {user_name}!")
    else:
        await update.message.reply_text("Пожалуйста, выберите кнопку из меню.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(API_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Бот запущен...")
    app.run_polling()












