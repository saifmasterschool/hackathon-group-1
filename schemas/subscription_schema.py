from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database.extension import Base


class Subscription(Base):
    __tablename__ = 'subscriptions'

    def __repr__(self):
        return f"<Subscription(phone_number='{self.phone_number}', channel_id={self.channel_id})>"

    def __str__(self):
        return f"Subscription: Phone Number={self.phone_number}, Channel ID={self.channel_id}"

    phone_number = Column(String, ForeignKey('users.phone_number'), primary_key=True)
    channel_id = Column(Integer, ForeignKey('channels.channel_id'), primary_key=True)

    # Relationships
    user = relationship('User', back_populates='subscriptions')
    channel = relationship('Channel', back_populates='subscriptions')
