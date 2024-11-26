import time

from config import MESSAGE_FETCH_INTERVAL
from sms_manager import DataManager

# Create SMS-manager
sms_manager = DataManager()

# Receive messages in a timed-interval
while True:
    received_messages = sms_manager.get_messages()
    print(received_messages)
    time.sleep(MESSAGE_FETCH_INTERVAL)
