from config import MASTERSCHOOL_API_TEAMNAME, AVAILABLE_CHANNELS, KEYWORD_JOIN_CHANNEL

WELCOME_MESSAGE = f"""Welcome to {MASTERSCHOOL_API_TEAMNAME}!
Subscribe to our variety of services by sending following message:
"{KEYWORD_JOIN_CHANNEL} <service>". While <service> can be one of the following:
{", ".join(AVAILABLE_CHANNELS)} (e.g. {KEYWORD_JOIN_CHANNEL} {AVAILABLE_CHANNELS[0]}).
Write JOKE to receive a joke instantly."""


BROADCAST_WATER_REMINDER_MESSAGE = """Hi, Please your water.
Otherwise you'll surely die! You forget it three times already. Calling an ambulance."""

'''BROADCAST_WATER_REMINDER_MESSAGE = """💧 Hey, hydration hero! 💧
It's time for a water break! Remember: your body is 70% water, not coffee or soda.
 This is your friendly reminder: DRINK UP!💦
 Stay hydrated. Stay alive. Conquer the day! 🌟"""

BROADCAST_JOKE_MESSAGE = """Get 3 daily doses of hilarity to keep the stress at bay!"""

BROADCAST_QUOTE_MESSAGE = """3 inspiring quotes a day to keep you motivated and unstoppable."""

STATUS_MESSAGE = """📊 Here's your subscription status:
- Subscribed to: {", ".join(USER_SUBSCRIPTIONS)}.
- Not subscribed yet? Pick your favorite from: {", ".join(AVAILABLE_CHANNELS)}.
Want to switch it up? Just send:
"{KEYWORD_JOIN_CHANNEL} <service>" or "STOP <service>" to unsubscribe.
Stay awesome and stay connected! ✨"""

WELCOME_MESSAGE = f"""🎉 Welcome to {MASTERSCHOOL_API_TEAMNAME}! 🎉
We've got some amazing services to brighten your day! Here's how you can join the fun:

👉 To subscribe, just send: "{KEYWORD_JOIN_CHANNEL} <service>".
For example: "{KEYWORD_JOIN_CHANNEL} {AVAILABLE_CHANNELS[0]}".

Here's what we offer:
✨ JOKE: Get 3 daily doses of hilarity to keep the stress at bay!
✨ QUOTE: 3 inspiring quotes a day to keep you motivated and unstoppable.
✨ WATER: A reminder to hydrate and refresh yourself.

Don't wait—join a service now and make your day awesome! 😊
"""'''