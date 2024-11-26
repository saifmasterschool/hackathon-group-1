import time

from config import MESSAGE_FETCH_INTERVAL
from external_api.jokes import get_joke_from_api
from data_managers import SMSDataManager, SQLiteDataManger
from utils.validation import validate_message

# Create Database-Manager
sqlite_manager = SQLiteDataManger()

# Create SMS-manager
sms_manager = SMSDataManager()


def start_message_loop():
    # Receive messages in a timed-interval
    # Basic usage example
    while True:
        print("---------------- LOOP OF MESSAGES: START ---------------")
        messages_in_api = sum(
            len(msgs)
            for message_dict in sms_manager.get_messages()
            for msgs in message_dict.values()
        )
        messages_in_database = len(sqlite_manager.get_messages())
        print(f"Of {messages_in_api} received messages in the api have {messages_in_database} already been handled.")

        # Get the timestamp of the last message
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
                sms_manager.send_sms(message.get("sender"), get_joke_from_api(), "Daily Joke from DailyMoodBoost")

            # ------------------------------------------------ #

            # Add message sqlite to mark as handled
            sqlite_manager.add_message_to_log(message)

        time.sleep(MESSAGE_FETCH_INTERVAL)
        print("---------------- LOOP OF MESSAGES: END ---------------")


if __name__ == "__main__":
    start_message_loop()
