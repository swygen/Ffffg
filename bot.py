from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ChatMemberHandler, ContextTypes

BOT_TOKEN = "7374304016:AAEp8gBPqt7Mxm6B8lU-qLea8jLFHD7FT-E"
ADMIN_ID = 6243881362

WELCOME_TEXT = """
Swygen Help
Welcome {name},
যেকোনো প্রয়োজনে যোগাযোগ করুন - @Swygen_bd

Our Services:
• Tournament App (Popular🔥)
• Android App
• Website
• Digital Marketing etc.

Username: {username}
Joining: {join_time}
"""

async def welcome_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_member.new_chat_member.user
    if user.is_bot:
        return
    
    name = user.first_name
    username = user.username or "N/A"
    join_time = update.chat_member.date.strftime("%d/%m/%Y %H:%M:%S")
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Send Message", url=f"https://t.me/{context.bot.username}?start=msg_admin")]
    ])

    await context.bot.send_message(
        chat_id=update.chat_member.chat.id,
        text=WELCOME_TEXT.format(name=name, username=username, join_time=join_time),
        reply_markup=keyboard
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "/start" and context.args and context.args[0] == "msg_admin":
        await context.bot.send_message(chat_id=ADMIN_ID, text=f"New user wants to contact you: @{update.effective_user.username}")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(ChatMemberHandler(welcome_message, ChatMemberHandler.CHAT_MEMBER))
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
