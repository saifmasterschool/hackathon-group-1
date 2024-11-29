from handlers.message_handler import handle_message
from task_scheduler import TaskScheduler

task_scheduler = TaskScheduler()


def test_subscribe_team():
    message = {
        "sender": "0123456789",
        "text": "SUBSCRIBE DailyMoodBoost",
        "receivedAt": "2024-11-26 12:39:53.266000"
    }

    assert handle_message(message, task_scheduler) == "SUBSCRIBED SUCCESSFULLY"


def test_unsubscribe_team():
    message = {
        "sender": "491746897704",
        "text": "UNSUBSCRIBE DailyMoodBoost",
        "receivedAt": "2024-11-26 12:39:53.266000"
    }

    assert handle_message(message, task_scheduler) == "UNSUBSCRIBED SUCCESSFULLY"


def test_unsubscribe_team_wrong_team():
    message = {
        "sender": "0123456789",
        "text": "UNSUBSCRIBE ASDASD",
        "receivedAt": "2024-11-26 12:39:53.266000"
    }

    assert handle_message(message, task_scheduler) == "FAILED TO UNSUBSCRIBE"
