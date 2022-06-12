from random import choice
import telebot

token = '5114938412:AAH9_YJs1J8eefrqMGa4x2cLHBilXisfFbI'

bot = telebot.TeleBot(token)

RANDOM_TASKS = [
    'get an advanced python course in netology',
    'write a message to Gvido van Rossum',
    'shaping, pinan sono ni and knife from both hands',
    'wash out a car',
    'replenish automation, selenium wd',
    'replenish API using python with json, requests',
    'replenish API using Postman'
]

todos = dict()

HELP = """
List of accessible commands:
* print - print out all tasks on given date
* todo - add a task
* random - add a task on today
* print out help
"""


def add_todo(date, task):
    date = date.lower()
    if todos.get(date) is not None:
        todos[date].append(task)
    else:
        todos[date] = []
        todos[date].append(task)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['random'])
def random(message):
    task = choice(RANDOM_TASKS)
    add_todo('today', task)
    bot.send_message(message.chat.id, f'Task {task} added on today')

@bot.message_handler(commands=['add'])
def add(message):
    _, date, tail = message.text.split(maxsplit=2)
    task = ' '.join([tail])
    # TODO: 1
    if len(task) < 3:
        bot.send_message(message.chat.id, 'Tasks can not be <= 3 chars')
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Task {task} added on day {date}')

@bot.message_handler(commands=['print'])
def print_(message):
    # TODO: 2
    dates = message.text.split(maxsplit=1)[1].lower().split()
    response  = ''
    for date in dates:
        tasks = todos.get(date)
        response += f'{date}: \n'
        for task in tasks:
            response += f'[ ] {task}\n'
        response += '\n'
    bot.send_message(message.chat.id, response)

bot.polling(none_stop=True)