import time

from config import MESSAGE_FETCH_INTERVAL, WELCOME_MESSAGE, KEYWORD_JOIN_CHANNEL
from data_managers import SMSDataManager, SQLiteDataManger
from external_api.jokes import get_joke_from_api
from handlers import join_channel, subscribe_team
from utils.information import print_worked_on_messages
from utils.validation import validate_message

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

            # Convert phone_number to int
            message = {**message, "sender": int(message["sender"])}

            # Check if message is already handled
            if sqlite_manager.check_if_message_handled(message):
                continue

            # ------------ Add message handlers here ---------- #
            # Handle the message based on the content
            handle_message(message)
            # ------------------------------------------------ #

            # Add message sqlite to mark as handled
            sqlite_manager.add_message_to_log(message)

        # Pause for the set amount of time before starting the next loop.
        time.sleep(MESSAGE_FETCH_INTERVAL)
        print("---------------- LOOP OF MESSAGES: END ---------------")


def handle_message(message):
    """
    Handles the message based on the text-content.
    Creates user-entries in the database to track channel subscriptions.
    :param message: The message received from the Masterschool SMS API.
    """
    if "SUBSCRIBE" in message["text"]:
        return subscribe_team(message, sms_manager)

    if KEYWORD_JOIN_CHANNEL in message["text"]:
        return join_channel(message, sms_manager, sqlite_manager)

    if "joke" in message["text"].lower():
        print(f"Sending joke to {message["sender"]}")
        return sms_manager.send_sms(
            message.get("sender"),
            get_joke_from_api(),
            "Daily Joke from DailyMoodBoost"
        )


if __name__ == "__main__":
    start_message_loop()
