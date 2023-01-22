from logger import logger
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from constants import constants, message_constants


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning('effective chat is None')
        return
    await context.bot.send_message(
        chat_id=effective_chat.id,
        text=message_constants.GREETINGS
    )


async def about_author(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.info('effective chat is None')
        return
    await context.bot.send_message(
        chat_id=effective_chat.id,
        text=message_constants.AUTHOR
    )


if __name__ == '__main__':
    application = ApplicationBuilder().token(constants.TELEGRAM_TOKEN).build()

    start_handler = CommandHandler('start', start)
    author_handler = CommandHandler('author', about_author)
    application.add_handler(start_handler)
    application.add_handler(author_handler)

    application.run_polling()
