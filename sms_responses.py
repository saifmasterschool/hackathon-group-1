from config import MASTERSCHOOL_API_TEAMNAME, AVAILABLE_CHANNELS, KEYWORD_JOIN_CHANNEL

WELCOME_MESSAGE = f"""Welcome to {MASTERSCHOOL_API_TEAMNAME}!
Subscribe to our variety of services by sending following message:
"{KEYWORD_JOIN_CHANNEL} <service>". While <service> can be one of the following:
{", ".join(AVAILABLE_CHANNELS)} (e.g. {KEYWORD_JOIN_CHANNEL} {AVAILABLE_CHANNELS[0]}).
Write JOKE to receive a joke instantly."""


STATUS_MESSAGE = f"""
Current status of {MASTERSCHOOL_API_TEAMNAME} services:
Available channels: {", ".join(AVAILABLE_CHANNELS)}.
You can also write JOKE or QUOTE to instantly receive a joke or a motivational quote.
"""



BROADCAST_WATER_REMINDER_MESSAGE = """Hi, Please your water.
Otherwise you'll surely die! You forget it three times already. Calling an ambulance."""

BROADCAST_JOKE_MESSAGE = """Get daily doses of jokes to keep you stress free!"""

BROADCAST_QUOTE_MESSAGE = """2 inspiring quotes a day to keep you motivated!"""
