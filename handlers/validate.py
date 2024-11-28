def validate_time_format(time_str: str) -> bool:
    """
    Validates that the given string is in HH:MM format (24-hour clock).
    :param time_str: The time string to validate.
    :return: True if the format is correct, otherwise False.
    """
    import re
    return re.match(r"^([01]\d|2[0-3]):[0-5]\d$", time_str) is not None
