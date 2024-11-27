from datetime import datetime, timedelta
from typing import Type

from sqlalchemy.orm import joinedload

from database.extension import Session
from schemas import Message, User


def get_messages() -> list[Type[Message]]:
    """
    Returns all messages.
    :return: All messages.
    """
    session = Session()
    try:
        messages = session.query(Message).all()
        return messages
    finally:
        session.close()


def check_if_message_handled(received_message) -> Message:
    """
    Returns the last created message with that receivedAt and sender combination.
    :param received_message: The message to check.
    :return: The potential message.
    """
    session = Session()

    try:
        exists = session.query(Message).filter(
            Message.sender == received_message["sender"],
            Message.receivedAt == received_message["receivedAt"]
        ).first()
        return exists
    finally:
        session.close()


def get_last_message_timestamp() -> datetime:
    """
    Returns a date object of the last received message.
    :return: A date object.
    """
    session = Session()

    try:
        last_message = session.query(Message).order_by(Message.receivedAt.desc()).first()
    finally:
        session.close()

    if last_message:
        return last_message.created_at
    else:
        date = datetime.now() - timedelta(days=5)
        return date


def add_message_to_log(received_message) -> Message:
    """
    Adds a handled message to the message log.
    :param received_message: The received message that needs to be added to the log.
    :return: The added message.
    """
    session = Session()

    try:
        message = Message(
            message=received_message["text"],
            sender=received_message["sender"],
            receivedAt=received_message["receivedAt"]
        )

        session.add(message)
        session.commit()
        return message
    finally:
        session.close()


def add_user(phone_number: int, channels: list[str]) -> User:
    """
    Adds a new user to the database.
    :param phone_number: the phone number of the user.
    :param channels: The channels the user is subscribed to.
    :return: The created user.
    """
    session = Session()

    try:
        user = User(
            phone_number=phone_number,
            channels=channels
        )
        session.add(user)
        session.commit()
        return user
    finally:
        session.close()


def get_users() -> list[Type[User]]:
    """
    Retrieves all users from the database.
    :return: All users in the database.
    """
    session = Session()

    try:
        return session.query(User).options(joinedload(User.channels), joinedload(User.custom_schedules)).all()
    finally:
        session.close()


def add_completed_drinking(phone_number):
    pass


def get_user_by_phone_number(phone_number: int) -> User:
    """
    Returns the user with the specified phone number.
    :param phone_number: The phone number of the user.
    :return: The user from the database.
    """
    session = Session()

    try:
        return session.query(User).filter(User.phone_number == phone_number).first()
    finally:
        session.close()


def get_users_by_channel(channel: str) -> list[Type[User]]:
    """
    Returns all users who are subscribed to specified channel.
    :param channel: The channel to filter by.
    :return: A list of all the users subscribed to that channel.
    """
    session = Session()

    try:
        return session.query(User).filter(User.channels.contains(channel)).all()
    finally:
        session.close()


def get_channels_of_user(phone_number: int) -> list[str]:
    """
    Returns all Channels a user is subscribed to.
    :param phone_number: The phone number of the user.
    :return: A list of channels.
    """
    session = Session()

    try:
        user = session.query(User).filter(User.phone_number == phone_number).first()
        if user:
            return user["channels"]
        return []
    finally:
        session.close()


def update_user_channels(phone_number: int, channels: list[str]) -> User:
    """
    Updates the channels of a user.
    :param phone_number: The users phone number.
    :param channels: A list of new channels
    :return: The updated user.
    """
    session = Session()

    try:
        user = session.query(User).filter(User.phone_number == phone_number).one()
        user.channels = channels
        session.commit()
        return user
    finally:
        session.close()
