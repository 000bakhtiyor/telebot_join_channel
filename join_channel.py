# ☪️ 𝔡𝔬𝔫𝔦𝔢𝔳


from telebot import *

channel_name = "CHANNEL_USER_NAME"   # Kanalingiz userini kiritasiz.
bot = TeleBot("BOT_TOKEN")           # Botingiz tokenini kiritasiz.

@bot.message_handler(commands=['start'])
def start(message):
    human = message.from_user.id
    humans_in_channel = bot.get_chat_member(channel_name,human)
    if humans_in_channel.status != "left":
        bot.send_message(message.chat.id , "True")
    else:
        bot.send_message(message.chat.id,"False")
    
    

bot.polling()
