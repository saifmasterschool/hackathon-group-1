from datetime import datetime


def convert_timestamp(timestamp_str):
    """
    Takes in a string representing a date and converts it into a python date object.
    Has to be of format: "%Y-%m-%dT%H:%M:%S.%f%z"
    :param timestamp_str: The string representing a date.
    :return: A Python date object
    """
    return datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%f%z").replace(tzinfo=None)
