import requests

from config import MASTERSCHOOL_API, MASTERSCHOOL_API_TEAMNAME


class DataManager:
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
    def get_messages():
        return requests.get(f'{MASTERSCHOOL_API}/team/getMessages/{MASTERSCHOOL_API_TEAMNAME}').json()

    @staticmethod
    def send_sms(phone_number, message, sender):
        return requests.post(f'{MASTERSCHOOL_API}/sms/send', json={
            "phoneNumber": phone_number,
            "message": message,
            "sender": sender
        }).json()
