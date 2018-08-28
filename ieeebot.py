import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from handlers import *
from settings import BOT_TOKEN

updater = Updater(token=BOT_TOKEN, workers=4)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

dispatcher.add_handler(CommandHandler('adminekle', add_admin_handler, pass_args=True))
dispatcher.add_handler(CommandHandler('soruekle', add_answer_handler, pass_args=True))
dispatcher.add_handler(MessageHandler(Filters.sticker, sticker_handler))

dispatcher.add_handler(
    ConversationHandler(entry_points=[CommandHandler('soru', question_handler)],
                        states={
                            CATEGORIES: [CallbackQueryHandler(callback_handler_categories, pattern="^cat")],

                            TAGS: [CallbackQueryHandler(callback_handler_tags, pattern="^tag"),
                                   CallbackQueryHandler(callback_handler_back, pattern="^geri")],

                        },
                        fallbacks=[CallbackQueryHandler(callback_handler_categories, pattern="^geri")]))

updater.start_polling()
