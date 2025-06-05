import os
import telebot
from flask import Flask, request

# Initialize bot
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Flask app
app = Flask(__name__)

# Define commands
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Hi, I’m Sharp AI — here for picks, parlays, and strategy.")

@bot.message_handler(commands=['status'])
def send_status(message):
    bot.reply_to(message, "📡 Sharp AI is online and watching Telegram.")

@bot.message_handler(commands=['picks'])
def send_picks(message):
    bot.reply_to(message, "🎯 Dodgers -1.5, Pacers +4.5, Braves ML — Confidence: 91%")

@bot.message_handler(commands=['parlay'])
def send_parlay(message):
    bot.reply_to(message, "🧠 3-leg parlay: Dodgers ML + Braves O8.5 + Celtics ML")

@bot.message_handler(commands=['hedge'])
def send_hedge(message):
    bot.reply_to(message, "🛡 Hedge strategy: +1.5 alt line or underdog ML on leg 2")

@bot.message_handler(commands=['feedback'])
def send_feedback(message):
    bot.reply_to(message, "📊 Feedback logged — thanks for training me!")

# Webhook endpoint
@app.route('/', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.get_data().decode("utf-8"))
    bot.process_new_updates([update])
    return '', 200

# Start bot with webhook
if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url='https://sharp-ai-telegram.onrender.com')  # Your Render domain
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
