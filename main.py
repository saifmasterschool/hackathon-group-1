import threading
import time

from config import MESSAGE_FETCH_INTERVAL
from data_managers import sms_manager, sqlite_manager
from database.extension import Base, engine
from database.init import init_database
from handlers.message_handler import handle_message
from task_scheduler import TaskScheduler, setup_scheduler
from utils.information import print_handled_messages
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
        print_handled_messages()

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
            handle_message(message, taskScheduler)
            # ------------------------------------------------ #

            # Add message sqlite to mark as handled
            sqlite_manager.add_message_to_log(message)

        # Pause for the set amount of time before starting the next loop.
        time.sleep(MESSAGE_FETCH_INTERVAL)
        print("---------------- LOOP OF MESSAGES: END ---------------")


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
