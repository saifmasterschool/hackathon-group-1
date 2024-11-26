import time

from config import MESSAGE_FETCH_INTERVAL
from sms_manager import SMSDataManager
from sqlite_manager import SQLiteDataManger

from external_api.jokes import get_joke_from_api

# Create Database-Manager
sqlite_manager = SQLiteDataManger()

# Create SMS-manager
sms_manager = SMSDataManager()

# Receive messages in a timed-interval
# Basic usage example
while True:
    received_messages: list[dict] = sms_manager.get_messages()
    handled_messages: list[Message]
    print(received_messages)

    # loop through all messages
    for message in received_messages:
        try:
            sender_number = int(message["sender"])
        except ValueError:
            print("Sender number is not convertable to number")
            continue

        # Handle the message based on the content
        if "joke" in message["text"].lower():
            sms_manager.send_sms(sender_number, get_joke_from_api(), "DailyMoodBoost")

        # TODO: Add the message to some kind of log (preferably sqlite) to prevent it from handling multiple times.

    time.sleep(MESSAGE_FETCH_INTERVAL)
