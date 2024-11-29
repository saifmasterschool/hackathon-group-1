from config import AVAILABLE_CHANNELS
from data_managers import sms_manager, sqlite_manager
from task_scheduler import schedule_dispatcher
from .validate import validate_time_format


def change_scheduler(message, task_scheduler):
    _, channel, *time_slots = message["text"].split(" ")
    phone_number = message["sender"]

    if channel.upper() not in AVAILABLE_CHANNELS:
        return sms_manager.send_sms(
            phone_number=message["sender"],
            message=f"Invalid channel '{channel}'. Available channels are: {', '.join(AVAILABLE_CHANNELS)}."
        )

    user = sqlite_manager.get_user_by_phone_number(phone_number)
    if channel not in [
        c.channel_name
        for c in user.channels
    ]:
        print(f"Custom schedule not applied, user is not in channel {channel}")
        return sms_manager.send_sms(
            phone_number=message["sender"],
            message=f"You have not joined '{channel}'. Join by sending a SMS with JOIN {channel}."
        )

    invalid_slots = [
        time_slot
        for time_slot in time_slots
        if not validate_time_format(time_slot)
    ]

    if invalid_slots:
        return sms_manager.send_sms(
            phone_number=message["sender"],
            message=f"Invalid time slot(s): {', '.join(invalid_slots)}. Please provide times in HH:MM format."
        )

    # Update the user's schedule in the database
    old_time_slots = sqlite_manager.update_user_schedule(message["sender"], channel.upper(), time_slots)

    # remove tasks from the task_scheduler
    for time_slot in old_time_slots.split(" "):
        task_scheduler.remove_task(
            f"{message["sender"]}_{channel}_{time_slot}"
        )

    # add new tasks to the task_scheduler
    for slot in time_slots:
        task_scheduler.add_task(
            slot,
            lambda: schedule_dispatcher[channel](message["sender"]),
            channel,
            message["sender"]
        )

    # Send confirmation to the user
    return sms_manager.send_sms(
        phone_number=message["sender"],
        message=f"Your schedule for '{channel}' has been updated to: {', '.join(time_slots)}."
    )
