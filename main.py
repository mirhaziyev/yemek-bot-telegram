import warnings
from similiarity import compare_txt
import time
import telebot
from telebot import types

warnings.filterwarnings('ignore')
TOKEN = 'your token'

bot = telebot.TeleBot(TOKEN)
print(bot)

# handle commands, /start
@Client.on_message(New.message(pattern="/start", incoming=True)
def handle_command(event):
    await event.reply("Salam, telegram bota xoş gəlmisiniz!")


# handle all messages, echo response back to users
@Client.on_message(New.message)
def handle_all_message(event):
    try:
        txt = compare_txt(message.text)[0]
        img = compare_txt(message.text)[2]
        hazirlanmasi = compare_txt(message.text)[1]
        text = "*{}*".format(txt) + hazirlanmasi
        await event.send_message(chat_id=message.chat.id, photo=img, caption=text)
    except:
        txt = compare_txt(message.text)
        await event.send_message(chat_id=message.chat.id,text=txt)

bot.polling()
# while True:
#   try:
#     bot.polling()
#   except Exception:
#     time.sleep(4)
#     print('not working')
