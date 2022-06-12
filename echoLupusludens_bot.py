import telebot

token = '5114938412:AAH9_YJs1J8eefrqMGa4x2cLHBilXisfFbI'

bot = telebot.TeleBot(token)

myName = 'Vic'

@bot.message_handler(content_types=["text"])
def echo(message):
    if myName.lower() in message.text.lower():
        text = f'Wow! Are you still here, {myName}?)!'
    else:
        text = message.text
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)