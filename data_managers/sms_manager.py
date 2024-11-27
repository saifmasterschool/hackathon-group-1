import requests

from config import MASTERSCHOOL_API, MASTERSCHOOL_API_TEAMNAME
from utils.dates import convert_timestamp


# TODO: Write an exception_handler decorator.
def create_team(team_name=MASTERSCHOOL_API_TEAMNAME):
    """
    Creates the team. Only needs to be used once after locking in the team-name.
    :param team_name: The team name. Defaults to the name defined in the config.
    :return: The MS API Server response.
    """
    return requests.post(f'{MASTERSCHOOL_API}/team/addNewTeam', json={
        "teamName": team_name
    }).json()


def register_phone_number_to_team(phone_number, team):
    """
    Registers
    :param phone_number:
    :param team:
    :return:
    """
    return requests.post(f'{MASTERSCHOOL_API}/team/registerNumber', json={
        "phoneNumber": phone_number,
        "teamName": team
    }).json()


def unregister_phone_number_from_team(phone_number, team):
    """
    Unregisters a phone number from team.
    :param phone_number: The phone number to unregister.
    :param team: The team name to unregister from.
    :return: The MS API response.
    """
    return requests.post(f'{MASTERSCHOOL_API}/team/registerNumber', json={
        "phoneNumber": phone_number,
        "teamName": team
    }).json()


def get_messages(team_name=MASTERSCHOOL_API_TEAMNAME):
    """
    Gets all unconverted messages from the MS API in a ridiculous format.
    :param team_name: The name of the team to fetch the messages for. Defaults to the name in the config file.
    :return: The MS API response.
    """
    return requests.get(f'{MASTERSCHOOL_API}/team/getMessages/{team_name}').json()


def get_filtered_messages(timestamp, team_name=MASTERSCHOOL_API_TEAMNAME) -> list[dict]:
    """
    Fetches all messages from the MS API and filters them by receivedAt date by given timestamp.
    Converts the result into list[dict]
    :param timestamp: A python date object.
    :param team_name: The name of the team to get the messages for.
    :return: The converted list of fetched messages.
    """
    messages_from_api = requests.get(f'{MASTERSCHOOL_API}/team/getMessages/{team_name}').json()
    return [
        {
            **message,
            "sender": int(sender),
            "receivedAt": convert_timestamp(message["receivedAt"])
        }
        for message_dict in messages_from_api
        for sender, messages in message_dict.items()
        for message in messages
        if convert_timestamp(message["receivedAt"]) > timestamp
    ]


def send_sms(phone_number, message, sender=""):
    """
    Sends an SMS.
    :param phone_number: The number of the recipient.
    :param message: The message to send.
    :param sender: [Not actually working, MS API bug] Define a sender name for the sms.
    :return: The MS API response.
    """
    return requests.post(f'{MASTERSCHOOL_API}/sms/send', json={
        "phoneNumber": phone_number,
        "message": message,
        "sender": sender
    }).json()
