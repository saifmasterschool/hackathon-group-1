import requests
from datetime import datetime

from config import SOCCER_API, SOCCER_API_KEY, SOCCER_API_FULL

headers = {
    'X-RapidAPI-Key': SOCCER_API_KEY,
    'X-RapidAPI-Host': SOCCER_API
}


def get_next_match(team_name):
    search_team_url = f"{SOCCER_API_FULL}/teams?name={team_name}"
    team_response = requests.get(search_team_url, headers=headers)
    team_data = team_response.json()

    if team_data['results'] > 0:
        team_id = team_data['response'][0]['team']['id']

        fixtures_url = f"{SOCCER_API_FULL}/fixtures?team={team_id}&next=1"
        fixtures_response = requests.get(fixtures_url, headers=headers)
        fixtures_data = fixtures_response.json()

        if fixtures_data['results'] > 0:
            next_fixture = fixtures_data['response'][0]
            match_date = next_fixture['fixture']['date']

            date_obj = datetime.fromisoformat(match_date[:-6])

            day = int(date_obj.strftime("%d"))
            if 4 <= day <= 20 or 24 <= day <= 30:
                suffix = "th"
            else:
                suffix = ["st", "nd", "rd"][day % 10 - 1]

            final_date = f"{day}{suffix} of {date_obj.strftime('%B %Y at %H:%M')}"

            return f"The next game of {team_name} is at {final_date}."
        else:
            return "No upcoming matches found"
    else:
        return f"Couldn't find a team with the name {team_name}."


if __name__ == "__main__":
    print(get_next_match("Hamburger SV"))
