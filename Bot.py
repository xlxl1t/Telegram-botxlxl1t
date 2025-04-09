import telebot
import os

# Telegram bot token (BotFather'dan olingan tokenni bu yerga joylashtiring)
API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

bot = telebot.TeleBot(API_TOKEN)

# Xabar yuborish funksiyasi
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men sizga kerakli postlarni yuboraman. Faqat kalit so'zni yuboring.")

# Kalit so'zga javob qaytarish
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Bu yerda siz postni topish va yuborish logikasini o‘rnatasiz
    bot.reply_to(message, f"Siz so'ragan post: {message.text}")

# Botni ishga tushurish
bot.polling()