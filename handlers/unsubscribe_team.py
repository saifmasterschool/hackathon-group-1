from data_managers import sms_manager
from config import MASTERSCHOOL_API_TEAMNAME


def unsubscribe_team(message):
    # Extract sender's phone number from the message
    phone_number = message.get("sender")
    
    # Unregister the phone number from the team
    response = sms_manager.unregister_phone_number_from_team(phone_number, MASTERSCHOOL_API_TEAMNAME)
    
    # Check if the unregistration was successful
    if response.get("success"):
        # Send a confirmation SMS to the user
        sms_manager.send_sms(
            phone_number = phone_number,
            message = "You have been successfully unsubscribed from our service. Thank you!"
        )
        print(f"User {phone_number} has been unsubscribed.")
    else:
        # Handle failure in unregistration (e.g., user not found)
        sms_manager.send_sms(
            phone_number = phone_number,
            message = "We could not process your unsubscription request. Please try again later."
        )
        print(f"Failed to unsubscribe user {phone_number}. Response: {response}")
    
    
    
