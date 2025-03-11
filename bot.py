from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import openai
import os

# Set OpenAI API Key
openai.api_key = os.getenv("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")

# Start command
async def start(update: Update, context):
    await update.message.reply_text("Hello! I am your AI Bot. Ask me anything.")

# Handle messages
async def handle_message(update: Update, context):
    user_message = update.message.text

    # Get response from OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    reply_text = response["choices"][0]["message"]["content"]
    await update.message.reply_text(reply_text)

# Main function
def main():
    app = ApplicationBuilder().token(os.getenv("7850771542:AAH4zkNOaUPUshvWi0huSviwOjleMekXsg4")).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
