from data_managers import sqlite_manager, sms_manager
from external_api import get_quote_from_api, get_joke_from_api
from sms_responses import BROADCAST_WATER_REMINDER_MESSAGE


def broadcast_water_reminder():
    """
    Sends a sms to remind people to drink water.
    """

    # Fetch all subscribed users that need to be reminded to drink
    users = sqlite_manager.get_users_by_channel("WATER")

    for user in users:
        print("WATER MESSAGE TO: ", user.phone_number)
        sms_manager.send_sms(
            phone_number=user["phone_number"],
            message=BROADCAST_WATER_REMINDER_MESSAGE
        )


def broadcast_joke():
    """
    Sends a joke to the user to boost a mood.
    """
    users = sqlite_manager.get_users_by_channel("JOKE")

    for user in users:
        sms_manager.send_sms(
            phone_number=user["phone_number"],
            message=get_joke_from_api()
        )


def broadcast_quote():
    """
    Sends an SMS to subscribed users with a daily quote
    """

    # Fetch all subscribed users who need to receive quotes
    users = sqlite_manager.get_users_by_channel("QUOTE")

    for user in users:
        sms_manager.send_sms(
            phone_number=user["phone_number"],
            message=get_quote_from_api()
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
    setup_broadcasts(task_scheduler)


def generate_function(phone_number, channel):
    return schedule_dispatcher[channel](phone_number)


def setup_broadcasts(task_scheduler):
    # Schedules for drinking water
    for time_slot in ["08:00", "10:00", "12:00", "14:00"]:
        task_scheduler.add_task(
            time_slot,
            broadcast_water_reminder,
            "WATER",
            "BROADCAST"
        )

    # Schedules for jokes
    for time_slot in ["10:00", "15:00", "20:00"]:
        task_scheduler.add_task(
            time_slot,
            broadcast_joke,
            "JOKE",
            "BROADCAST"
        )

    # Schedules for quotes
    for time_slot in ["09:30", "16:30", "20:00"]:
        task_scheduler.add_task(
            time_slot,
            broadcast_quote,
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


def individual_message(phone_number, message):
    return sms_manager.send_sms(
        phone_number,
        message
    )
