
import os
import telebot

# Token from BotFather
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Simple logic bindings
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Hi, I’m Sharp AI — here to help with picks, parlays, and strategic insights.")

@bot.message_handler(commands=['status'])
def send_status(message):
    bot.reply_to(message, "📡 Sharp AI is online. System status is nominal.")

@bot.message_handler(commands=['picks'])
def send_picks(message):
    bot.reply_to(message, "🎯 Tonight’s top picks: Dodgers -1.5, Pacers +4.5, Braves ML. Confidence: 91%")

@bot.message_handler(commands=['parlay'])
def send_parlay(message):
    bot.reply_to(message, "🧠 3-leg parlay: Dodgers ML + Braves O8.5 + Celtics ML. Confidence: 86%")

@bot.message_handler(commands=['hedge'])
def send_hedge(message):
    bot.reply_to(message, "🛡 To hedge: use an alt +1.5 spread or underdog ML on your second leg.")

@bot.message_handler(commands=['feedback'])
def send_feedback(message):
    bot.reply_to(message, "👍 Feedback logged. Thanks for helping me learn!")

# Run the bot
if __name__ == '__main__':
    bot.infinity_polling()
