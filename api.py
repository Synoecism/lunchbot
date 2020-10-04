import requests

# get chat_id

def send_message(token, chatid, message):

    method = 'https://api.telegram.org/bot' + token + \
        '/sendMessage?chat_id=' + chatid + '&text=' + message
    response = requests.get(method)

    return response.json()

def delete_message(token, chatid, messageid):

    method = 'https://api.telegram.org/bot' + token + \
        '/deleteMessage?chat_id=' + chatid + '&message_id=' + messageid
    response = requests.get(method)

    return response.json()
