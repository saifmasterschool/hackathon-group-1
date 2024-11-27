"""
Contents of this file should be saved in a ".env" file, but
sharing envs can be pretty cumbersome, especially in a public repository.
So for now, everything's saved in a config file, probably updated before finishing.
"""

from os import path

MASTERSCHOOL_API = "http://hackathons.masterschool.com:3030"
MASTERSCHOOL_API_TEAMNAME = "DailyMoodBoost"

MESSAGE_FETCH_INTERVAL = 20

basedir = path.abspath(path.dirname(__file__))
SQLite_file = f'sqlite:///{path.join(basedir, "database", "dailyMoodBoost.sqlite")}'

JOKES_API = "https://v2.jokeapi.dev/joke/Any?type=single"
QUOTES_API = "https://zenquotes.io/api/random"


KEYWORD_JOIN_CHANNEL = "JOIN"
KEYWORD_LEAVE_CHANNEL = "LEAVE"

AVAILABLE_CHANNELS = ["WATER", "JOKE", "QUOTE"]


