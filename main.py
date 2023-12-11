import json

from telethon import TelegramClient, events

with open('settings.json') as conf:
    config = json.load(conf)


api_id = "26419931"
api_hash = "3cc6fc47db62bd0b93be5f0f6b991e98"

if __name__ == '__main__':
    client = TelegramClient('redmes', api_id, api_hash)

    @client.on(events.NewMessage(chats=config['chatsInput']))
    async def normal_handler(event):
        user_mess = event.message.to_dict()['message']
        s_user_id = event.message.to_dict()['from_id']
        users_id = s_user_id.get('user_id')
        user = users.get(str(users_id) + str(event.message.to_dict()['peer_id'].get('chat_id')))

        await client.send_message(config['userOutput'], user + "Message: " + user_mess)

    users = {}
    client.start()

    for chat in config['chatsInput']:
        chatID = -1
        for chat_id in client.iter_dialogs():
            if (chat_id.title == chat):
                chatID = chat_id.id * -1

        participants = client.get_participants(chat)
        for partic in client.iter_participants(chat):
            lastName = ""
            if partic.last_name:
                lastName = partic.last_name
            users[str(partic.id) + str(chatID)] = "Chat: " + chat + "\nUser: " + partic.first_name + " " + lastName + "\n"

    client.run_until_disconnected()

