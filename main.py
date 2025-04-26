import asyncio
from telegram.ext import Application
from config import BOT_TOKEN
from bot.handlers import setup_handlers
from bot.jobs import setup_jobs
from bot.utils import log

async def main():
    log("Bot sedang mulai...")
    application = Application.builder().token(BOT_TOKEN).build()
    setup_handlers(application)
    setup_jobs(application)
    log("Bot siap!")
    await application.run_polling()

if __name__ == '__main__':
    while True:
        try:
            asyncio.run(main())
        except Exception as e:
            log(f"Error: {e}")
            log("Bot restart ulang...")
