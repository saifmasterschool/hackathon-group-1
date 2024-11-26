import time

from config import MESSAGE_FETCH_INTERVAL
from sms_manager import SMSDataManager
from sqlite_manager import SQLiteDataManger

# Create Database-Manager
sqlite_manager = SQLiteDataManger()

# Create SMS-manager
sms_manager = SMSDataManager()

# Receive messages in a timed-interval
while True:
    received_messages = sms_manager.get_messages()
    print(received_messages)
    time.sleep(MESSAGE_FETCH_INTERVAL)
