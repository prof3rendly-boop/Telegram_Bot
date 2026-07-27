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

LINK = "https://drive.google.com/file/d/1I8kXqNrefDhAr9g7XpHZ0sAHm9qQPgEE/view?usp=sharing"

KEY = """2026-07-31 17:03|2D28-DBC9-4584-087D-CB35-067A-70DD-BAF6"""

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
