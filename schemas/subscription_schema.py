from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database.extension import Base


class Subscription(Base):
    __tablename__ = 'subscriptions'

    phone_number = Column(String, ForeignKey('users.phone_number'), primary_key=True)
    channel_id = Column(Integer, ForeignKey('channels.channel_id'), primary_key=True)

    # Relationships
    user = relationship('User', back_populates='subscriptions')
    channel = relationship('Channel', back_populates='subscriptions')
