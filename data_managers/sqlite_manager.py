from datetime import datetime, timedelta
from functools import cache
from typing import Type

from sqlalchemy.orm import joinedload

from utils.decorators import with_session

from database.extension import Session
from schemas import Message, User, Subscription, Channel, CustomSchedule


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
        date = datetime.now() - timedelta(seconds=30)
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


def add_user(phone_number: int) -> User:
    """
    Adds a new user to the database.
    :param phone_number: the phone number of the user.
    :return: The created user.
    """
    session = Session()

    try:
        user = User(
            phone_number=phone_number
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


def get_subscriptions_of_user(phone_number):
    session = Session()

    try:
        return session.query(Subscription).filter(Subscription.phone_number == phone_number).all()
    finally:
        session.close()


def get_custom_schedules():
    session = Session()

    try:
        query = session.query(CustomSchedule).options(
            joinedload(CustomSchedule.user),
            joinedload(CustomSchedule.channel)
        ).all()

        return query
    finally:
        session.close()


def update_user_schedule(phone_number: int, channel_name: str, time_slots: list[str]) -> str:
    """
    Updates the user's schedule for a specific channel.
    :param phone_number: The phone number of the user.
    :param channel_name: The name of the channel to update.
    :param time_slots: A list of time slots (in HH:MM format) for the schedule.
    """
    session = Session()

    try:
        # get the channel id
        channel_id = get_channel_id(channel_name).channel_id

        # get all custom schedules for a user
        custom_schedule = session.query(
            CustomSchedule
        ).filter(
            CustomSchedule.phone_number == phone_number,
            CustomSchedule.channel_id == channel_id
        ).first()

        if custom_schedule:
            old_time_slots = custom_schedule.schedule

            # update the slots
            custom_schedule.schedule = " ".join(time_slots)
        else:
            old_time_slots = ""
            session.add(CustomSchedule(
                phone_number=phone_number,
                channel_id=channel_id,
                schedule=" ".join(time_slots)
            ))

        session.commit()

        return old_time_slots
    finally:
        session.close()


@cache
def get_channel_id(channel_name) -> Channel:
    session = Session()

    try:
        return session.query(Channel).filter(Channel.channel_name == channel_name).first()
    finally:
        session.close()


def add_completed_drinking(phone_number, receivedAt):
    pass


def get_user_by_phone_number(phone_number: int) -> User:
    """
    Returns the user with the specified phone number.
    :param phone_number: The phone number of the user.
    :return: The user from the database.
    """
    session = Session()

    try:
        return session.query(
            User
        ).options(
            joinedload(
                User.channels
            )
        ).filter(
            User.phone_number == phone_number
        ).first()
    finally:
        session.close()


def get_users_by_channel(channel_name: str) -> list[Type[User]]:
    """
    Returns all users who are subscribed to specified channel.
    :param channel_name: The channel to filter by.
    :return: A list of all the users subscribed to that channel.
    """
    session = Session()

    try:
        channel_with_users = session.query(Channel).options(
            joinedload(
                Channel.users
            ).joinedload(
                User.custom_schedules
            )
        ).filter(
            Channel.channel_name == channel_name
        ).first()

        if channel_with_users:
            return channel_with_users.users

        return []
    finally:
        session.close()


def get_channels_of_user(phone_number: int) -> list[Type[Channel]]:
    """
    Returns all Channels a user is subscribed to.
    :param phone_number: The phone number of the user.
    :return: A list of channels.
    """
    session = Session()

    try:
        user = session.query(User).options(
            joinedload(
                User.channels
            )
        ).filter(User.phone_number == phone_number).first()

        if user:
            return user.channels
        return []
    finally:
        session.close()


def add_subscription(phone_number: int, channel_id: int) -> User:
    """
    Updates the channels of a user.
    :param phone_number: The users phone number.
    :param channel_id: The new channel_id
    :return: The updated user.
    """
    session = Session()

    try:
        session.add(Subscription(
            phone_number=phone_number,
            channel_id=channel_id
        ))

        session.commit()

        return session.query(User).options(
            joinedload(
                User.channels
            )
        ).filter(User.phone_number == phone_number).first()
    finally:
        session.close()


def remove_subscription(phone_number, channel_id):
    session = Session()

    try:
        subscription = session.query(Subscription).filter(
            Subscription.phone_number == phone_number,
            Subscription.channel_id == channel_id
        ).first()

        if subscription:
            session.delete(subscription)
            session.commit()
    finally:
        session.close()
