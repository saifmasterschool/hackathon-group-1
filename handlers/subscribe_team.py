from sms_responses import WELCOME_MESSAGE
from data_managers import sms_manager


def subscribe_team(message):
    """
    Replies to the user after subscribing to the team-name.
    :param message: The user-message from the MS API.
    :return: Sends a message to the sender.
    """
    print(f"Replying to {message["sender"]} with subscription info")
    return sms_manager.send_sms(
        message.get("sender"),
        WELCOME_MESSAGE
    )
