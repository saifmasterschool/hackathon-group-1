from os import path

MASTERSCHOOL_API = "http://hackathons.masterschool.com:3030"
MASTERSCHOOL_API_TEAMNAME = "team_1_nov_2024"

MESSAGE_FETCH_INTERVAL = 20

basedir = path.abspath(path.dirname(__file__))
SQLite_file = f'sqlite:///{path.join(basedir, "database", "dailyMoodBoost.sqlite")}'

JOKES_API = "https://v2.jokeapi.dev/joke/Any?type=single"
