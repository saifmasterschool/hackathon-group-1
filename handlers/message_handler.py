import handlers
from config import KEYWORD_JOIN_CHANNEL, KEYWORD_LEAVE_CHANNEL
from data_managers import sms_manager
from external_api import get_joke_from_api, get_quote_from_api, get_next_match
from sms_responses import DEFAULT_MESSAGE


def handle_message(message, task_scheduler):
    """
    Handles the message based on the text-content.
    Creates user-entries in the database to track channel subscriptions.
    :param message: The message received from the Masterschool SMS API.
    :param task_scheduler: The taskScheduler instance.
    """
    message_text: str = message["text"].strip()
    phone_number: str = message["sender"]

    print("MESSAGE RECEIVED:", message_text, "from", phone_number)

    if message_text.startswith("SUBSCRIBE"):
        return handlers.subscribe_team(message)

    if message_text.startswith("UNSUBSCRIBE"):
        return handlers.unsubscribe_team(message)

    if message_text.startswith("STATUS"):
        return handlers.status_response(message)

    if message_text.startswith(KEYWORD_JOIN_CHANNEL):
        return handlers.join_channel(message)

    if message_text.startswith(KEYWORD_LEAVE_CHANNEL):
        return handlers.leave_channel(message)

    if message_text.startswith(("CHANGESCHEDULE", "CS")):
        return handlers.change_scheduler(message, task_scheduler)

    if message_text.startswith("WATER"):
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
