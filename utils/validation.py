def validate_message(message):
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
