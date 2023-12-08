import telebot
import requests
import asyncio

# from telethon.sync import TelegramClient
from telethon import TelegramClient, sync, events
# from telethon.tl.functions.messages import SendMessage

token = "6855197447:AAEHYJ708al27MiXpXDl1WZumHlP6I8vMwY"
chat_id = "1158333885"
bot = telebot.TeleBot(token)
# url = "https://api.telegram.org/bot=" + token + "/sendMessage?chat_id=" + chatID + "&text=123123"

api_id = "26419931"
api_hash = "3cc6fc47db62bd0b93be5f0f6b991e98"


# response = requests.get(url)

@bot.message_handler(commands=["start"])
async def print_hi(message):
    bot.send_message(message.chat.id, text="Привет, это бот!")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(chat_id=chat_id, text=message.text)


if __name__ == '__main__':
    # print_hi

    chatName = "ForProject"

    client = TelegramClient('redmes', api_id, api_hash)

    transport = ""

    @client.on(events.NewMessage(chats=(chatName)))
    async def normal_handler(event):
        print(event.message.to_dict()['message'])
        user_mess = event.message.to_dict()['message']
        s_user_id = event.message.to_dict()['from_id']
        users_id = s_user_id.get('user_id')
        user = users.get(users_id)
        mess_date = event.message.to_dict()['date']
        f = open('messages', 'a')
        f.write(mess_date.strftime("%d-%m-%Y %H:%M") + "\n")
        f.write(user + "\n")
        f.write(user_mess + "\n\n")
        f.flush()

    client.start()
    participants = client.get_participants(chatName)
    users = {}

    for partic in client.iter_participants(chatName):
        lastName = ""
        if partic.last_name:
            lastName = partic.last_name
        users[partic.id] = partic.first_name + " " + lastName

    for dialog in client.iter_dialogs():
        if (dialog.title == chatName):
            print(dialog.title)


    client.run_until_disconnected()


bot.polling()