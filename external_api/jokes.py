import requests

from config import JOKES_API


def get_joke_from_api() -> str:
    """
    Fetches a joke from the api configured in the config.
    :return: The joke as a string.
    """
    return requests.get(JOKES_API).json()["joke"]
