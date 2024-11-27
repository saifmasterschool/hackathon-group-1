from config import MASTERSCHOOL_API_TEAMNAME, AVAILABLE_CHANNELS, KEYWORD_JOIN_CHANNEL, KEYWORD_LEAVE_CHANNEL

WELCOME_MESSAGE = f"""Welcome to {MASTERSCHOOL_API_TEAMNAME}!
Subscribe to our variety of services by sending following message:
"{KEYWORD_JOIN_CHANNEL} <service>". While <service> can be one of the following:
{", ".join(AVAILABLE_CHANNELS)} (e.g. {KEYWORD_JOIN_CHANNEL} {AVAILABLE_CHANNELS[0]}).
Write JOKE to receive a joke instantly."""

STATUS_MESSAGE = f"""

"""

BROADCAST_WATER_REMINDER_MESSAGE = """This is your drinking reminder number 3. Please respond with "DRUNK 3" to confirm you drank your water"""

DEFAULT_MESSAGE = f"""Your message could not be recognised.
Use keywords SUBSCRIBE, UNSUBSCRIBE, STATUS, {KEYWORD_JOIN_CHANNEL} or {KEYWORD_LEAVE_CHANNEL}.
Or just write joke or quote to instantly receive a joke or quote ;)"""
