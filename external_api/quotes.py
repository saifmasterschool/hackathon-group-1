import requests

from config import QUOTES_API


def get_quote_from_api() -> str:
    """
    Fetches a quote from the API configured in the config.
    :return: The quote as a string.
    """
    return requests.get(QUOTES_API).json()["quote"]
