from datetime import datetime

import requests

from config import MASTERSCHOOL_API, MASTERSCHOOL_API_TEAMNAME


class SMSDataManager:
    @staticmethod
    def create_team(team_name):
        return requests.post(f'{MASTERSCHOOL_API}/team/addNewTeam', json={
            "teamName": MASTERSCHOOL_API_TEAMNAME
        })

    @staticmethod
    def register_phone_number_to_team(phone_number, team):
        return requests.post(f'{MASTERSCHOOL_API}/team/registerNumber', json={
            "phoneNumber": phone_number,
            "teamName": team
        }).json()

    @staticmethod
    def unregister_phone_number_from_team(phone_number, team):
        return requests.post(f'{MASTERSCHOOL_API}/team/registerNumber', json={
            "phoneNumber": phone_number,
            "teamName": team
        }).json()

    @staticmethod
    def get_messages(team_name=MASTERSCHOOL_API_TEAMNAME):
        return requests.get(f'{MASTERSCHOOL_API}/team/getMessages/{team_name}').json()

    @staticmethod
    def get_filtered_messages(timestamp, team_name=MASTERSCHOOL_API_TEAMNAME):
        messages_from_api = requests.get(f'{MASTERSCHOOL_API}/team/getMessages/{team_name}').json()
        return [
            message
            for message in messages_from_api
            if datetime.strptime(message.get("receivedAt"), __format="%Y-%m-%dT%H:%M:%S.%f%z") > timestamp
        ]

    @staticmethod
    def send_sms(phone_number, message, sender=""):
        return requests.post(f'{MASTERSCHOOL_API}/sms/send', json={
            "phoneNumber": phone_number,
            "message": message,
            "sender": sender
        }).json()
