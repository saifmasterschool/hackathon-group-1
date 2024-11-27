from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.orm import relationship

from database.extension import Base


class User(Base):
    __tablename__ = "users"

    def __repr__(self):
        return f"<User(phone_number={self.phone_number}, created_at='{self.created_at}', updated_at='{self.updated_at}')>"

    def __str__(self):
        return f"User: Phone Number={self.phone_number}, Created at: {self.created_at}, Updated at: {self.updated_at}"

    phone_number = Column(Integer, primary_key=True, nullable=False)

    subscriptions = relationship('Subscription', back_populates='user')
    channels = relationship('Channel', secondary='subscriptions', viewonly=True)
    custom_schedules = relationship('CustomSchedule', back_populates='user')

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
