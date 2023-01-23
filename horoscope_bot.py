from logger import logger
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from constants import constants, message_constants
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


async def close_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning('effective chat is None')
        return
    await context.bot.send_message(
        chat_id=effective_chat.id,
        text=start(update, context),
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning('effective chat is None')
        return
    await context.bot.send_message(
        reply_markup=ReplyKeyboardRemove(),
        chat_id=effective_chat.id,
        text=message_constants.GREETINGS,
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


async def signs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.info('effective chat is None')
        return
    marcup = ReplyKeyboardMarkup([['Aquarius', 'Saginarius'],
                                  ['Назад']], one_time_keyboard=False)
    await context.bot.send_message(
        reply_markup=marcup,
        chat_id=effective_chat.id,
        text='Все знаки зодиака',
    )


if __name__ == '__main__':
    application = ApplicationBuilder().token(constants.TELEGRAM_TOKEN).build()

    start_handler = CommandHandler('start', start)
    author_handler = CommandHandler('author', about_author)
    signs_handler = CommandHandler('signs', signs)
    application.add_handler(signs_handler)
    application.add_handler(start_handler)
    application.add_handler(author_handler)
    application.run_polling()
