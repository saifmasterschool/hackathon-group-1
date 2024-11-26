def validate_message(message):
    """
    Validates the message from the server. Has to have sender, receivedAt and text properties.
    :param message: The message from the MS Server.
    :return: Boolean value if message is valid.
    """
    message_keys = ["sender", "receivedAt", "text"]

    for key in message_keys:
        if key not in message.keys():
            return False
    try:
        int(message["sender"])
        return True
    except ValueError:
        print("Sender number is not convertable to number")
        return False
    except KeyError:
        print("Sender not in message")
        return False
