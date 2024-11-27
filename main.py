import threading
import time

import schedule

from config import MESSAGE_FETCH_INTERVAL, KEYWORD_JOIN_CHANNEL
from data_managers import sms_manager, sqlite_manager
from database.extension import Base, engine
from external_api.jokes import get_joke_from_api
from handlers import join_channel, subscribe_team
from utils.information import print_worked_on_messages
from utils.validation import validate_message


def start_message_loop():
    """
    Starts an infinite loop to receive all messages for the teamname from the Masterschool-Api.
    Filters the received messages to only work on new messages that haven't been handled.
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


def start_scheduler():
    """
    Start an infinite loop to execute scheduled jobs. Scheduled job in the context of our app are
    SMS reminders that users subscribed to.
    """
    while True:
        schedule.run_pending()
        time.sleep(1)


def broadcast_water_reminder():
    """
    Sends a sms to remind people to drink water.
    """

    # Fetch all subscribed users that need to be reminded to drink
    users = sqlite_manager.get_user_by_channel("WATER")
    for user in users:
        sms_manager.send_sms(
            phone_number=user["phone_number"],
            message="""Hi, Please drink water.
Otherwise you'll surely die! You forget it three times already. Calling an ambulance."""
        )


def broadcast_joke():
    """
    Sends a joke to user to boost a mood.
    """
    users = sqlite_manager.get_user_by_channel("JOKE")
    for user in users:
        sms_manager.send_sms(
            phone_number=user["phone_number"],
            message=f"""Here is your dose of humor:
{get_joke_from_api()}"""
        )


def broadcast_quote():
    """
    Sends an SMS to subscribed users with a daily quote
    """
    # Fetch all subscribed users who need to receive quotes
    users = sqlite_manager.get_user_by_channel("QUOTE")

    for user in users:
        sms_manager.send_sms(
            phone_number=user["phone_number"],
            message=f"""Hi, here's your daily dose of inspiration:
{get_quote_from_api()}"""
        )


# Schedules for drinking water
schedule.every().day.at("08:00").do(broadcast_water_reminder)
schedule.every().day.at("10:00").do(broadcast_water_reminder)
schedule.every().day.at("12:00").do(broadcast_water_reminder)
schedule.every().day.at("14:00").do(broadcast_water_reminder)

# Schedules for jokes
schedule.every().day.at("10:00").do(broadcast_joke)
schedule.every().day.at("12:00").do(broadcast_joke)
schedule.every().day.at("16:00").do(broadcast_joke)
schedule.every().day.at("20:00").do(broadcast_joke)
# Schedules for quotes
schedule.every().day.at("10:00").do(broadcast_quote)
schedule.every().day.at("12:00").do(broadcast_quote)
schedule.every().day.at("14:00").do(broadcast_quote)
schedule.every().day.at("18:00").do(broadcast_quote)
# schedule.every().day.at("17:00").do(job2)


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    # Put both loops of different threads since both use time.sleep and would otherwise cancel each other out.
    thread1 = threading.Thread(target=start_message_loop)
    thread2 = threading.Thread(target=start_scheduler)

    # Start the threads.
    thread1.start()
    thread2.start()
