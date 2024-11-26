from config import WELCOME_MESSAGE


def subscribe_team(message, sms_manager):
    """
    Replies to the user after subscribing to the team-name.
    :param message: The user-message from the MS API.
    :param sms_manager: The SMS DataManager.
    :return: Sends a message to the sender.
    """
    print(f"Replying to {message["sender"]} with subscription info")
    return sms_manager.send_sms(
        message.get("sender"),
        WELCOME_MESSAGE
    )
