from data_managers import sms_manager, sqlite_manager
from sms_responses import STATUS_MESSAGE


def status_response(message):
    user_subscriptions = sqllite

    sms_manager.send_sms(message["sender"], STATUS_MESSAGE(""))
