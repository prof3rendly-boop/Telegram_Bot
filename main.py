import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# Render Environment Variables kısmına BOT_TOKEN olarak ekle
TOKEN = os.getenv("BOT_TOKEN")

LINK = "https://drive.google.com/file/d/1I8kXqNrefDhAr9g7XpHZ0sAHm9qQPgEE/view"

KEY = """2026-08-12 14:17|8B87-FBBD-D0F5-6F88-1043-F3BC-5769-7460"""

WELCOME = """
👋 Hoş geldin!

Komutlar:

/link
/key
"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME)


async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🔗 Link:\n\n{LINK}")


async def key(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🔑 Key:\n\n{KEY}")


async def new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await update.message.reply_text(
            f"👋 Hoş geldin {user.first_name}!\n\n"
            f"Botu açıp /start yazarak komutları görebilirsin."
        )


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN bulunamadı.")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("link", link))
    app.add_handler(CommandHandler("key", key))

    app.add_handler(
        MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member)
    )

    print("Bot çalışıyor...")

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
