import requests
from sms_manager import DataManager

sms_manager = DataManager
received_messages = sms_manager.get_messages()
print(received_messages)
