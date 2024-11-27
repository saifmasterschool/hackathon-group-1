from data_managers import sqlite_manager, sms_manager
from config import AVAILABLE_CHANNELS


def leave_channel(message):
    phone_number = message["sender"]
    _, *channel = message["text"].split(" ")

    try:
        channel: str = channel[0]
    except IndexError:
        return sms_manager.send_sms(
            phone_number,
            """Please provide a Channel you want to unsubscribe from."""
        )

    if not channel:
        return sms_manager.send_sms(
            phone_number,
            """Please provide a Channel you want to unsubscribe from."""
        )

    if channel.upper() not in AVAILABLE_CHANNELS:
        print("leave channel: ", channel[0].upper())
        return sms_manager.send_sms(
            phone_number,
            """Please check the spelling of the channel you want to unsubscribe from"""
        )

    user = sqlite_manager.get_user_by_phone_number(phone_number)
    channel_names = [c.channel_name for c in user.channels]

    if not user or channel not in channel_names:
        return sms_manager.send_sms(
            phone_number,
            f"""You are not subscribed to channel {channel}."""
        )

    sqlite_manager.remove_subscription(
        phone_number,
        sqlite_manager.get_channel_id(channel).channel_id
    )

    sms_manager.send_sms(
        phone_number,
        f"""You successfully unsubscribed from {channel}"""
    )
