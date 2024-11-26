from config import AVAILABLE_CHANNELS


def join_channel(message, sms_manager, sqlite_manager):
    """
    If the message text includes the channel join keyword (e.g. JOIN), add the user to database
    or update the channel-list of the user.
    :param message: The message of the MS API.
    :param sms_manager: The SMS DataManager.
    :param sqlite_manager: The SQLite DataManger.
    :return: Send a message to the user.
    """
    # Define the phone_number from the message
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
        sqlite_manager.add_user(phone_number=phone_number, channels=channels)
    # Update the user otherwise.
    else:
        sqlite_manager.update_user_channels(phone_number=phone_number, channels=[*user["channels"], *channels])

    print(f"Replying to {message["sender"]} with a successfully joined broadcast message")
    sms_manager.send_sms(phone_number, f"Successfully joined {", ".join(channels)}. Welcome!")
