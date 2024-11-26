import time
from datetime import datetime, timedelta

from config import MESSAGE_FETCH_INTERVAL
from external_api.jokes import get_joke_from_api
from sms_manager import SMSDataManager
from sqlite_manager import SQLiteDataManger

# Create Database-Manager
sqlite_manager = SQLiteDataManger()

# Create SMS-manager
sms_manager = SMSDataManager()

# Receive messages in a timed-interval
# Basic usage example
while True:
    # Get the timestamp of the last message
    last_message_time_stamp = sqlite_manager.get_last_message_timestamp()

    # Filter all messages that only new messages are shown.
    received_messages: list[dict] = sms_manager.get_filtered_messages(last_message_time_stamp)

    print(received_messages)

    # loop through all messages
    for message in received_messages:
        try:
            sender_number = int(message["sender"])
        except ValueError:
            print("Sender number is not convertable to number")
            continue

        # Check if message is already handled
        if sqlite_manager.check_if_message_handled({**message, "sender": sender_number}):
            continue

        # ------------ Add message handlers here ---------- #
        # Handle the message based on the content
        if "joke" in message["text"].lower():
            sms_manager.send_sms(sender_number, get_joke_from_api(), "Daily Joke from DailyMoodBoost")

        # ------------------------------------------------ #

        # Add message sqlite to mark as handled
        sqlite_manager.add_message_to_log({**received_messages, "sender": sender_number})

    time.sleep(MESSAGE_FETCH_INTERVAL)
