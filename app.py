import os
import telebot
from flask import Flask

# 1. Token-ka wuxuu ka imaanayaa Render Environment Variables
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/')
def index():
    return "KaydAI Bot is running!"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Ku soo dhawaada KaydAI! Bot-kaagu hadda waa mid ammaan ah.")

if __name__ == "__main__":
    import threading
    threading.Thread(target=bot.infinity_polling).start()
    
    # Render wuxuu isticmaalaa Port-kan
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)