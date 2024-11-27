from data_managers import sqlite_manager, sms_manager
from sms_responses import STATUS_MESSAGE


def status_response(message):
    sqlite_manager.get_channels_of_user(message["sender"])

    sms_manager.send_sms(message["sender"], STATUS_MESSAGE)
