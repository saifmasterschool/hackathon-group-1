from config import MASTERSCHOOL_API_TEAMNAME, AVAILABLE_CHANNELS, KEYWORD_JOIN_CHANNEL, KEYWORD_LEAVE_CHANNEL

DEFAULT_MESSAGE = f"""Your message could not be recognised.
Use keywords SUBSCRIBE, UNSUBSCRIBE, STATUS, {KEYWORD_JOIN_CHANNEL} or {KEYWORD_LEAVE_CHANNEL}.
Or just write joke or quote to instantly receive a joke or quote ;)"""

BROADCAST_WATER_REMINDER_MESSAGE = """💧 Hey, hydration hero! 💧
It's time for a water break! Remember: your body is 70% water, not coffee or soda.
This is your friendly reminder: DRINK UP!💦
Stay hydrated. Stay alive. Conquer the day! 🌟"""

STATUS_MESSAGE = """📊 Here's your subscription status:
- Subscribed to: {", ".join(USER_SUBSCRIPTIONS)}.
- Not subscribed yet? Pick your favorite from: {", ".join(AVAILABLE_CHANNELS)}.
Want to switch it up? Just send:
"{KEYWORD_JOIN_CHANNEL} <service>" or "STOP <service>" to unsubscribe.
Stay awesome and stay connected! ✨
Current status of {MASTERSCHOOL_API_TEAMNAME} services:
Available channels: {", ".join(AVAILABLE_CHANNELS)}.
You can also write JOKE or QUOTE to instantly receive a joke or a motivational quote.
Also write GAME <team_name> to see the next fixture.
"""

WELCOME_MESSAGE = f"""🎉 Welcome to {MASTERSCHOOL_API_TEAMNAME}! 🎉
We've got some amazing services to brighten your day! Here's how you can join the fun:
👉 To subscribe, just send: "{KEYWORD_JOIN_CHANNEL} <service>".
For example: "{KEYWORD_JOIN_CHANNEL} {AVAILABLE_CHANNELS[0]}".
Here's what we offer:
✨ JOKE: Get 3 daily doses of hilarity to keep the stress at bay!
✨ QUOTE: 3 inspiring quotes a day to keep you motivated and unstoppable.
✨ WATER: A reminder to hydrate and refresh yourself.
Don't wait—join a service now and make your day awesome! 😊
"""
