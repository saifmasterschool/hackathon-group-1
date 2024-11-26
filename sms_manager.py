import requests

MASTERSCHOOL_API = "http://hackathons.masterschool.com:3030"
MASTERSCHOOL_API_TEAMNAME = "team_1_nov_2024"


class DataManager:
    @staticmethod
    def create_team(team_name):
        return requests.post(f'{MASTERSCHOOL_API}/team/addNewTeam', json={
            "teamName": MASTERSCHOOL_API_TEAMNAME
        })

    @staticmethod
    def register_phone_number_to_team(phone_number, team):
        return requests.post(f'{MASTERSCHOOL_API}')

    @staticmethod
    def get_messages():
        return requests.get(f'{MASTERSCHOOL_API}/team/getMessages/{MASTERSCHOOL_API_TEAMNAME}').json()
