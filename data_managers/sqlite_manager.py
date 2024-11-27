from datetime import datetime, timedelta
from typing import Type

from sqlalchemy import text

from database.extension import Session
from schemas import Message, User


def get_messages() -> list[Type[Message]]:
    session = Session()
    try:
        messages = session.query(Message).all()
        return messages
    finally:
        session.close()


def check_if_message_handled(received_message) -> Message:
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


def get_user_by_phone_number(phone_number: int) -> User:
    session = Session()

    try:
        return session.query(User).filter(User.phone_number == phone_number).first()
    finally:
        session.close()


def get_user_by_channel(channel: str) -> list[Type[User]]:
    session = Session()

    try:
        return session.query(User).filter(User.channels.contains(channel)).all()
    finally:
        session.close()


def update_user_channels(phone_number: int, channels: list[str]) -> User:
    session = Session()

    try:
        user = session.query(User).filter(User.phone_number == phone_number).one()
        user.channels = channels
        session.commit()
        return user
    finally:
        session.close()
