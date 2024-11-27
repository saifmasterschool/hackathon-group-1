from config import MASTERSCHOOL_API_TEAMNAME, AVAILABLE_CHANNELS, KEYWORD_JOIN_CHANNEL

WELCOME_MESSAGE = f"""Welcome to {MASTERSCHOOL_API_TEAMNAME}!
Subscribe to our variety of services by sending following message:
"{KEYWORD_JOIN_CHANNEL} <service>". While <service> can be one of the following:
{", ".join(AVAILABLE_CHANNELS)} (e.g. {KEYWORD_JOIN_CHANNEL} {AVAILABLE_CHANNELS[0]}).
Write JOKE to receive a joke instantly."""
