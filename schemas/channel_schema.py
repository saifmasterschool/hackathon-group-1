from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from database.extension import Base


class Channel(Base):
    __tablename__ = 'channels'

    def __repr__(self):
        return f"<Channel(channel_id={self.channel_id}, channel_name='{self.channel_name}')>"

    def __str__(self):
        return f"Channel: {self.channel_name} (ID: {self.channel_id})"

    channel_id = Column(Integer, primary_key=True, autoincrement=True)
    channel_name = Column(String)

    # Relationship to Subscription
    subscriptions = relationship('Subscription', back_populates='channel')
    # Get users vie subscriptions
    users = relationship('User', secondary='subscriptions', viewonly=True)
