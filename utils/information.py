from data_managers import sms_manager, sqlite_manager


def print_handled_messages():
    """
    Fetches all Messages saved in the Masterschool API Server and from the local database.
    Compares how many are already handled.

    :return: Prints the state in the console.
    """
    messages_in_api = sum(
        len(msgs)
        for message_dict in sms_manager.get_messages()
        for msgs in message_dict.values()
    )
    messages_in_database = len(sqlite_manager.get_messages())
    print(f"Of {messages_in_api} received messages in the api have {messages_in_database} already been handled.")
