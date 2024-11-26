from datetime import datetime

import requests

from config import MASTERSCHOOL_API, MASTERSCHOOL_API_TEAMNAME


class SMSDataManager:
    def __init__(self):
        self._requests = requests

    def create_team(self, team_name=MASTERSCHOOL_API_TEAMNAME):
        return self._requests.post(f'{MASTERSCHOOL_API}/team/addNewTeam', json={
            "teamName": team_name
        })

    def register_phone_number_to_team(self, phone_number, team):
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
        return [
            message
            for message in messages_from_api
            if datetime.strptime(message.get("receivedAt"), __format="%Y-%m-%dT%H:%M:%S.%f%z") > timestamp
        ]

    def send_sms(self, phone_number, message, sender=""):
        return self._requests.post(f'{MASTERSCHOOL_API}/sms/send', json={
            "phoneNumber": phone_number,
            "message": message,
            "sender": sender
        }).json()
