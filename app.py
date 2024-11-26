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
# Basic usage added
while True:
    received_messages: list[dict] = sms_manager.get_messages()
    print(received_messages)

    for message in received_messages:
        try:
            sender_number = int(message["sender"])
        except ValueError:
            print("Sender number is not convertable to number")
            continue

        if "joke" in message["text"].lower():
            sms_manager.send_sms(sender_number, get_joke_from_api(), "DailyMoodBoost")

    time.sleep(MESSAGE_FETCH_INTERVAL)
