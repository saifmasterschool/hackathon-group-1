import time

from config import MESSAGE_FETCH_INTERVAL
from external_api.jokes import get_joke_from_api
from data_managers import SMSDataManager, SQLiteDataManger
from utils.validation import validate_message
from utils.information import print_worked_on_messages

# Create Database-Manager
sqlite_manager = SQLiteDataManger()

# Create SMS-manager
sms_manager = SMSDataManager()


def start_message_loop():
    """
    Starts an infinite loop to receive all messages for the teamname from the Masterschool-Api.
    Filters the received messages to only work on new messages that havent been handled.
    Filters message texts provide correct functionality, e.g. adding senders to broadcast messages.
    """
    # Receive messages in a timed-interval
    # Basic usage example
    while True:
        print("---------------- LOOP OF MESSAGES: START ---------------")
        # Print the progress, mostly for debugging
        print_worked_on_messages(sms_manager, sqlite_manager)

        # Get the timestamp of the last message (from database)
        last_message_timestamp = sqlite_manager.get_last_message_timestamp()

        # Filter all messages that only new messages are shown.
        received_messages: list[dict] = sms_manager.get_filtered_messages(last_message_timestamp)

        # loop through all messages
        for message in received_messages:
            if not validate_message(message):
                print("Message has incorrect type.")
                continue

            message = {**message, "sender": int(message["sender"])}

            # Check if message is already handled
            if sqlite_manager.check_if_message_handled(message):
                continue

            # ------------ Add message handlers here ---------- #
            # Handle the message based on the content
            if "joke" in message["text"].lower():
                print(f"Sending joke to {message["sender"]}")
                sms_manager.send_sms(message.get("sender"), get_joke_from_api(), "Daily Joke from DailyMoodBoost")

            # ------------------------------------------------ #

            # Add message sqlite to mark as handled
            sqlite_manager.add_message_to_log(message)

        time.sleep(MESSAGE_FETCH_INTERVAL)
        print("---------------- LOOP OF MESSAGES: END ---------------")


if __name__ == "__main__":
    start_message_loop()
