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
    received_messages = sms_manager.get_messages()
    print(received_messages)

    # Error because of wrong documentation
    for [number, data] in received_messages.items():
        message = data["text"]

        if "joke" in message.lower():
            sms_manager.send_sms(number, get_joke_from_api(), "DailyMoodBoost")

    time.sleep(MESSAGE_FETCH_INTERVAL)
