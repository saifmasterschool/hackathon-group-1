from datetime import datetime, timedelta
from typing import Type

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import SQLite_file
from database.extension import Base
from schemas import Message, User


class SQLiteDataManger:
    def __init__(self):
        self.engine = create_engine(SQLite_file)
        self.session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.session()

    # TODO: add methods for users, routines and jokes
    def get_messages(self) -> list[Type[Message]]:
        session = self.get_session()
        try:
            messages = session.query(Message).all()
            return messages
        finally:
            session.close()

    def check_if_message_handled(self, received_message) -> Message:
        session = self.get_session()
        try:
            exists = session.query(Message).filter(
                Message.sender == received_message["sender"],
                Message.receivedAt == received_message["receivedAt"]
            ).first()
            return exists
        finally:
            session.close()

    def get_last_message_timestamp(self):
        session = self.get_session()
        try:
            last_message = session.query(Message).order_by(Message.created_at.desc()).first()
        finally:
            session.close()

        if last_message:
            return last_message.created_at
        else:
            date = datetime.now() - timedelta(days=5)
            return date

    def add_message_to_log(self, received_message):
        session = self.get_session()
        try:
            message = Message(
                message=received_message["text"],
                sender=received_message["sender"],
                receivedAt=received_message["receivedAt"]
            )

            session.add(message)
            session.commit()
        finally:
            session.close()

    def add_user(self, phone_number: int, channels: list[str]):
        session = self.get_session()
        try:
            user = User(
                phone_number=phone_number,
                channels=channels
            )
            session.add(user)
            session.commit()
        finally:
            session.close()

    def get_user_by_phone_number(self, phone_number: int):
        session = self.get_session()
        try:
            return session.query(User).filter(User.phone_number == phone_number).one()
        finally:
            session.close()

    def update_user_channels(self, phone_number: int, channels: list[str]):
        session = self.get_session()
        try:
            user = session.query(User).filter(User.phone_number == phone_number).one()
            user.channels = channels
            session.commit()
        finally:
            session.close()
