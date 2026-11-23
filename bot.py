
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "សួស្តី! សូមស្វាគមន៍មកកាន់ Khmer AI Video Translator 🇰🇭\n\n"
        "📥 ផ្ញើ Link Facebook ឬ TikTok ដើម្បីសាកល្បង។\n"
        "🎙 អ្នកក៏អាចផ្ញើឯកសារសំឡេង ឬវីដេអូបានផងដែរ។\n\n"
        "មុខងារ AI បកប្រែសំឡេងខ្មែរនឹងត្រូវបន្ថែមជាបន្តបន្ទាប់។"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "សូមអរគុណ! ❤️\n"
        "ប្រព័ន្ធកំពុងត្រូវបានរៀបចំ។ "
        "មុខងារទាញយក និងបកប្រែសំឡេងនឹងមកដល់ឆាប់ៗនេះ។"
    )

def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN is missing")

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
