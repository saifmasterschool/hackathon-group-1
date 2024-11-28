from data_managers import sqlite_manager
from data_managers.sms_manager import send_sms


def handle_drink_response(message):
    """
    Handles a user's water-related SMS.

    - Ensures the user is subscribed to the "WATER" channel.
    - If the SMS contains "WATER STATUS", sends a status update.
    - If the SMS contains "WATER <amount>", logs the water intake.
    - If the SMS contains "WATER GOAL <amount>", sets the daily goal.
    """
    
    phone_number = message["sender"]
    text = message["text"].strip().lower()
    
    user = sqlite_manager.get_user_by_phone_number(phone_number)
    if not user or "WATER" not in user.channels:
        send_sms(
            phone_number = phone_number,
            message = "You are not subscribed to the water intake service. "
                      "Send 'JOIN WATER' to subscribe."
        )
        return
    
    # Handle "WATER STATUS"
    if text == "water status":
        daily_goal = getattr(user, "daily_goal", 2000)  # Default goal is 2000ml
        total_consumed_today = sqlite_manager.get_total_water_consumed_today(phone_number)
        remaining_water = max(0, daily_goal - total_consumed_today)
        
        if remaining_water > 0:
            send_sms(
                phone_number = phone_number,
                message = f"You have consumed {total_consumed_today} ml out of your daily goal of {daily_goal} ml. "
                          f"You need {remaining_water} ml more to reach your goal. Keep hydrating!"
            )
        else:
            send_sms(
                phone_number = phone_number,
                message = f"Congratulations! You have met or exceeded your daily goal of {daily_goal} ml of water. "
                          f"Great job staying hydrated!"
            )
        return
    
    # Handle "WATER GOAL <amount>"
    if text.startswith("water goal "):
        try:
            new_goal = int(text.split("water goal ")[1])
            sqlite_manager.update_user_goal(phone_number, new_goal)
            send_sms(
                phone_number = phone_number,
                message = f"Your daily water intake goal has been updated to {new_goal} ml."
            )
            return
        except (ValueError, IndexError):
            send_sms(
                phone_number = phone_number,
                message = "Invalid format for setting goal. Please send 'WATER GOAL <amount>' (e.g., WATER GOAL 2500)."
            )
            return
    
    # Handle "WATER <amount>"
    if text.startswith("water "):
        try:
            water_amount = int(text.split("water ")[1])
            sqlite_manager.add_completed_drinking(
                phone_number = phone_number,
                timestamp = message["receivedAt"],
                amount = water_amount
            )
            send_sms(
                phone_number = phone_number,
                message = f"Your water intake of {water_amount} ml has been logged successfully. "
                          f"Keep hydrating!"
            )
            return
        except (ValueError, IndexError):
            send_sms(
                phone_number = phone_number,
                message = "Invalid format for logging water. Please send 'WATER <amount>' (e.g., WATER 500)."
            )
            return
    
    # If no valid command is found
    send_sms(
        phone_number = phone_number,
        message = "Invalid format. Please send:\n"
                  "'WATER <amount>' to log your intake\n"
                  "'WATER GOAL <amount>' to set your goal\n"
                  "'WATER STATUS' to check your progress"
    )