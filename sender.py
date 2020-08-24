# https://pupli.net/2019/02/get-chat-id-from-telegram-bot/ -- how to find chat id
# https://github.com/bostrot/telegram-support-bot/issues/16 -- supergroup question
# https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e -- setup the bot

import requests
import os
from getter import getText
import datetime
BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']


def telegram_bot_sendtext(bot_message):

    bot_token = BOT_TOKEN
    bot_chatID = CHAT_ID
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


# get dayOfWeek (functions starts at 0, 0 = monday but using 1 as monday)
dayOfWeek = datetime.datetime.today().weekday()+1

test = telegram_bot_sendtext(getText(dayOfWeek))
