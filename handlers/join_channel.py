from config import AVAILABLE_CHANNELS
from data_managers import sms_manager, sqlite_manager


def join_channel(message):
    """
    If the message text includes the channel join keyword (e.g. JOIN), add the user to database
    or update the channel-list of the user.
    :param message: The message of the MS API.
    :return: Send a message to the user.
    """
    # Get the phone number from the message
    phone_number = message["sender"]

    # Select the channel
    _, *channels = message["text"].split(" ")

    # If no channel is given, reply with error
    if len(channels) < 1:
        return sms_manager.send_sms(
            phone_number=phone_number,
            message="""Please select a channel to join"""
        )

    # Check if correct Channel is selected
    for channel in channels:
        if channel not in AVAILABLE_CHANNELS:
            return sms_manager.send_sms(
                phone_number=phone_number,
                message=f"Channel {channel} is not a valid channel."
            )

    # Select the user by phone number from the database.
    user = sqlite_manager.get_user_by_phone_number(phone_number)

    # Create the user if not exist.
    if not user:
        sqlite_manager.add_user(phone_number=phone_number)

    user_channels_ids = set(
        subscription.channel_id
        for subscription in sqlite_manager.get_subscriptions_of_user(phone_number)
    )

    new_channel_ids = set(
        sqlite_manager.get_channel_id(channel).channel_id
        for channel in channels
    )

    for channel_id in new_channel_ids.difference(user_channels_ids):
        # Update the channels of the user.
        sqlite_manager.add_subscription(phone_number=phone_number, channel_id=channel_id)

    print(f"Replying to {message["sender"]} with a successfully joined broadcast message")
    sms_manager.send_sms(phone_number, f"Successfully joined {", ".join(channels)}. Welcome!")
