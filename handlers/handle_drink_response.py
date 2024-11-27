from data_managers import sqlite_manager


def handle_drink_response(message):
    # 1: Add to database
    # 2: Response is amount of successfully drinking
    amount_of_successful_drinks = sqlite_manager.add_completed_drinking(message["sender"], message["receivedAt"])

    # TODO: Check if the number of drinks drank > proposed drinks and send message based on taht.

    # 2: Send a sms with the number of drinks he took this day
    # sms_send()
