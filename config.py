from os import path

MASTERSCHOOL_API = "http://hackathons.masterschool.com:3030"
MASTERSCHOOL_API_TEAMNAME = "DailyMoodBoost"

MESSAGE_FETCH_INTERVAL = 20

basedir = path.abspath(path.dirname(__file__))
SQLite_file = f'sqlite:///{path.join(basedir, "database", "dailyMoodBoost.sqlite")}'

JOKES_API = "https://v2.jokeapi.dev/joke/Any?type=single"

KEYWORD_JOIN_CHANNEL = "JOIN"
AVAILABLE_CHANNELS = ["WATER", "JOKE", "QUOTE"]

WELCOME_MESSAGE = f"""Welcome to {MASTERSCHOOL_API_TEAMNAME}!
Subscribe to our variety of services by sending following message:
"{KEYWORD_JOIN_CHANNEL} <service>". While <service> can be one of the following:
{", ".join(AVAILABLE_CHANNELS)} (e.g. {KEYWORD_JOIN_CHANNEL} {AVAILABLE_CHANNELS[0]}).
Write JOKE to receive a joke instantly."""
