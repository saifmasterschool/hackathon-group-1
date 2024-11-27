from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from database.extension import Base


class Channel(Base):
    __tablename__ = 'channels'

    channel_id = Column(Integer, primary_key=True, autoincrement=True)
    channel_name = Column(String)

    # Relationship to Subscription
    subscriptions = relationship('Subscription', back_populates='channel')
    # Get users vie subscriptions
    users = relationship('User', secondary='subscriptions', viewonly=True)
