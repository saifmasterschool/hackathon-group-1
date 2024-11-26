import requests

from config import MASTERSCHOOL_API, MASTERSCHOOL_API_TEAMNAME
from utils.dates import convert_timestamp


# TODO: Write an exception_handler decorator.
class SMSDataManager:
    def __init__(self):
        """
        Initialises the app. Basically unnecessary, but having all @staticmethods looks weird.
        """
        self._requests = requests

    def create_team(self, team_name=MASTERSCHOOL_API_TEAMNAME):
        """
        Creates the team. Only needs to be used once after locking in the team-name.
        :param team_name: The team name. Defaults to the name defined in the config.
        :return: The MS API Server response.
        """
        return self._requests.post(f'{MASTERSCHOOL_API}/team/addNewTeam', json={
            "teamName": team_name
        }).json()

    def register_phone_number_to_team(self, phone_number, team):
        """

        :param phone_number:
        :param team:
        :return:
        """
        return self._requests.post(f'{MASTERSCHOOL_API}/team/registerNumber', json={
            "phoneNumber": phone_number,
            "teamName": team
        }).json()

    def unregister_phone_number_from_team(self, phone_number, team):
        return self._requests.post(f'{MASTERSCHOOL_API}/team/registerNumber', json={
            "phoneNumber": phone_number,
            "teamName": team
        }).json()

    def get_messages(self, team_name=MASTERSCHOOL_API_TEAMNAME):
        return self._requests.get(f'{MASTERSCHOOL_API}/team/getMessages/{team_name}').json()

    def get_filtered_messages(self, timestamp, team_name=MASTERSCHOOL_API_TEAMNAME):
        messages_from_api = self._requests.get(f'{MASTERSCHOOL_API}/team/getMessages/{team_name}').json()
        res_messages = [
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

        return res_messages

    def send_sms(self, phone_number, message, sender=""):
        return self._requests.post(f'{MASTERSCHOOL_API}/sms/send', json={
            "phoneNumber": phone_number,
            "message": message,
            "sender": sender
        }).json()
