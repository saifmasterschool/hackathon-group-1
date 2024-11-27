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

    if channel[0].upper() not in AVAILABLE_CHANNELS:
        return sms_manager.send_sms(
            phone_number,
            """Please check the spelling of the channel you want to unsubscribe from"""
        )

    user = sqlite_manager.get_user_by_phone_number(phone_number)

    if not user:
        return sms_manager.send_sms(
            phone_number,
            """You are not subscribed to any channels"""
        )

    sqlite_manager.update_user_channels(
        phone_number,
        [c for c in user.channels if c != channel]
    )

    sms_manager.send_sms(
        phone_number,
        f"""You successfully unsubscribed from {channel}"""
    )
