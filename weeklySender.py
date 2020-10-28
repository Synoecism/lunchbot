from api import *
from getter import getDailyInWeek
from decouple import config
import os
import time
import json
import datetime

def main():

    # get local environment variable
    BOT_TOKEN = config('BOT_TOKEN')
    CHAT_ID = config('CHAT_ID')

    # check if should use global environment variables
    if BOT_TOKEN is None:
        BOT_TOKEN = os.environ['BOT_TOKEN']
        CHAT_ID = os.environ['CHAT_ID']
    else:
        print("Status: using local variables")

    messageText = "Veckans meny:"
    for x in range (1,6):
        # get text from getter
        messageText = messageText + "\n" + "\n" + getDailyInWeek(x)

    # send a message to chat
    res = send_message(BOT_TOKEN, CHAT_ID, messageText)

    # get message id from response
    message_id = res['result']['message_id']

    # create txt file
    file = open("message.txt","w+")

    # save message_id in txt file
    file.write(str(message_id))

if __name__ == "__main__":
    main()
