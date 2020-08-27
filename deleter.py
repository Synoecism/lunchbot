from api import *
from getter import getText
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

    # open txt file
    file = open("message.txt","r")

    # read message id from file
    message_id = file.read()

    # delete message by id
    delete_message(BOT_TOKEN,CHAT_ID,message_id)

if __name__ == "__main__":
    main()
