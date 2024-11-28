import threading
import time

from config import MESSAGE_FETCH_INTERVAL, KEYWORD_JOIN_CHANNEL, KEYWORD_LEAVE_CHANNEL, AVAILABLE_CHANNELS
from data_managers import sms_manager, sqlite_manager
from database.extension import Base, engine
from database.init import init_database
from external_api import get_quote_from_api, get_joke_from_api, get_next_match
import handlers
from sms_responses import DEFAULT_MESSAGE
from task_scheduler import TaskScheduler, setup_scheduler, individual_message, schedule_dispatcher
from utils.information import print_worked_on_messages
from utils.validation import validate_message

# Initialize TaskScheduler
taskScheduler = TaskScheduler()


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
    print("MESSAGE RECEIVED:", message["text"], "from", message["sender"])
    if "SUBSCRIBE" in message["text"]:
        return handlers.subscribe_team(message)

    if "UNSUBSCRIBE" in message["text"]:
        return handlers.unsubscribe_team(message)

    if "STATUS" in message["text"]:
        return handlers.status_response(message)

    if KEYWORD_JOIN_CHANNEL in message["text"]:
        return handlers.join_channel(message)

    if KEYWORD_LEAVE_CHANNEL in message["text"]:
        return handlers.leave_channel(message)

    if "CHANGESCHEDULE" in message["text"] or "CS" in message["text"]:
        return handlers.change_scheduler(message, taskScheduler)

    if "DRUNK" in message["text"]:
        return handlers.handle_drink_response(message)

    if "joke" in message["text"].lower():
        print(f"Sending joke to {message["sender"]}")
        return sms_manager.send_sms(
            message.get("sender"),
            get_joke_from_api(),
            "Daily Joke from DailyMoodBoost"
        )

    if "GAME" in message["text"]:
        _, *team_name = message["text"].split(" ")
        team_name = " ".join(team_name)
        next_match = get_next_match(team_name)

        print("next match", next_match)

        return sms_manager.send_sms(
            message["sender"],
            next_match
        )

    if "quote" in message["text"].lower():
        print(f"Sending quote to {message['sender']}")
        return sms_manager.send_sms(
            message.get("sender"),
            get_quote_from_api(),
            "Daily Quote from DailyMoodBoost"
        )

    return sms_manager.send_sms(
        phone_number=message["sender"],
        message=DEFAULT_MESSAGE
    )


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    # Init database and taskScheduler
    init_database()
    setup_scheduler(taskScheduler)

    # Put both loops of different threads since both use time.sleep and would otherwise cancel each other out.
    thread1 = threading.Thread(target=start_message_loop)
    thread2 = threading.Thread(target=taskScheduler.run_pending)

    # Start the threads.
    thread1.start()
    thread2.start()
