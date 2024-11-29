from data_managers import sms_manager, sqlite_manager
from sms_responses import STATUS_MESSAGE


def status_response(message):
    phone_number = message["sender"]
    user_subscriptions = [
        subscription.channel_name
        for subscription in sqlite_manager.get_channels_of_user(phone_number)
    ]

    status_message = STATUS_MESSAGE(user_subscriptions)
    print(f"Sending status message to {phone_number}", "subscriptions:", user_subscriptions)

    sms_manager.send_sms(phone_number, status_message)
