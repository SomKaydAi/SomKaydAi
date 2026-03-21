import os
import telebot
from flask import Flask

# 1. Halkan code-ku isagaa Render ka soo akhrisanaya Token-ka
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# 2. Flask wuxuu u baahan yahay Render si uu u ogaado in bot-ku nool yahay
app = Flask(__name__)

@app.route('/')
def index():
    return "KaydAI Bot is running!"

# 3. Marka qofku bilaabo bot-ka (/start)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Ku soo dhawaada KaydAI! Bot-kaagu hadda waa mid ammaan ah.")

# 4. Inuu bot-ku dhageysto farriimaha (Polling)
if __name__ == "__main__":
    import threading
    threading.Thread(target=bot.infinity_polling).start()
    
    # Port-ka uu Render bixiyo
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
