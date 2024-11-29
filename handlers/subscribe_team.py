from sms_responses import WELCOME_MESSAGE
from data_managers import sms_manager, sqlite_manager


def subscribe_team(message):
    """
    Replies to the user after subscribing to the team-name.
    :param message: The user-message from the MS API.
    :return: Sends a message to the sender.
    """
    phone_number = message["sender"]

    print(f"Replying to {phone_number} with subscription info")

    user = sqlite_manager.get_user_by_phone_number(phone_number)

    if user:
        channels = [
            channel.channel_name
            for channel in sqlite_manager.get_channels_of_user(phone_number)
        ]

        return sms_manager.send_sms(
            phone_number,
            f"""Welcome back. Your subscription settings are restored. ({", ".join(channels)})"""
        )

    sms_manager.send_sms(
        message.get("sender"),
        WELCOME_MESSAGE
    )

    return "SUBSCRIBED SUCCESSFULLY"
