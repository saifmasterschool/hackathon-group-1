from data_managers import sqlite_manager, sms_manager
from external_api import get_quote_from_api, get_joke_from_api
from sms_responses import BROADCAST_WATER_REMINDER_MESSAGE


def broadcast_message(channel: str, message: str):
    """
    Sends a broadcast-message to a channel.
    :param channel: The channel to send the broadcast-message to.
    :param message: The message to send.
    """

    print(f"Broadcast message to channel {channel}")

    # Fetch all subscribed users that need to be reminded to drink
    broadcast_users = [
        user
        for user in sqlite_manager.get_users_by_channel(channel)
        if not user.custom_schedules
    ]

    for user in broadcast_users:
        print("Broadcast message sent to: ", user.phone_number)
        sms_manager.send_sms(
            phone_number=user["phone_number"],
            message=message
        )


def individual_message(phone_number, message):
    print(f"Sending individual scheduled message to {phone_number}")
    return sms_manager.send_sms(
        phone_number,
        message
    )


def setup_scheduler(task_scheduler):
    # Fetches all custom schedules
    custom_schedules = sqlite_manager.get_custom_schedules()

    # Loop over the schedules
    for custom_schedule in custom_schedules:
        channel = custom_schedule.channel.channel_name
        phone_number = custom_schedule.user.phone_number

        for time_slot in custom_schedule.schedule.split(" "):
            task_scheduler.add_task(
                time_slot,
                lambda: schedule_dispatcher[channel](phone_number),
                channel,
                phone_number
            )

    # Init default scheduled reminders
    setup_scheduler_for_default_broadcasts(task_scheduler)


def setup_scheduler_for_default_broadcasts(task_scheduler):
    # Schedules for drinking water
    for time_slot in ["08:00", "10:00", "12:00", "14:00", "16:50"]:
        task_scheduler.add_task(
            time_slot,
            lambda: broadcast_message("WATER", BROADCAST_WATER_REMINDER_MESSAGE),
            "WATER",
            "BROADCAST"
        )

    # Schedules for jokes
    for time_slot in ["10:00", "15:00", "20:00"]:
        task_scheduler.add_task(
            time_slot,
            lambda: broadcast_message("JOKE", get_joke_from_api()),
            "JOKE",
            "BROADCAST"
        )

    # Schedules for quotes
    for time_slot in ["09:30", "16:30", "20:00"]:
        task_scheduler.add_task(
            time_slot,
            lambda: broadcast_message("QUOTE", get_quote_from_api()),
            "QUOTE",
            "BROADCAST"
        )


schedule_dispatcher = {
    "WATER": lambda phone_number: individual_message(
        phone_number,
        BROADCAST_WATER_REMINDER_MESSAGE
    ),
    "JOKE": lambda phone_number: individual_message(
        phone_number,
        get_joke_from_api()
    ),
    "QUOTE": lambda phone_number: individual_message(
        phone_number,
        get_quote_from_api()
    ),
}
