import telebot

# Halkan waa Token-kaagii rasmiga ahaa
TOKEN = "8299416894:AAG2YUeUq6qGQPiNCDadNJt5QQHqrVMwIDs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "🌟 **Kusoo dhawaaw SomKaydAi Intelligence!** 🚀\n\n"
        "Waxaan ahay AI-gii ugu horreeyay ee loogu talagalay "
        "horumarinta iyo kaydinta aqoonta Soomaaliyeed.\n\n"
        "Sideen kuu caawin karaa maanta?"
    )
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Halkan waxaan ku diyaarinaynaa jawaabaha AI-ga
    user_query = message.text
    response = f"SomKaydAi ayaa helay fariintaada: '{user_query}'. " \
               f"Weli waxaan ku jiraa wejigii tababarka (Training), " \
               f"laakiin dhowaan ayaan si buuxda u jawaabi doonaa!"
    bot.reply_to(message, response)

print("SomKaydAi Bot is now running...")
bot.infinity_polling()
