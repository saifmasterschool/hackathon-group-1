from datetime import datetime


def convert_timestamp(timestamp_str):
    return datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%f%z").replace(tzinfo=None)
