from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database.extension import Base


class CustomSchedule(Base):
    __tablename__ = 'custom_schedules'

    def __repr__(self):
        return f"<Channel(channel_id={self.channel_id}, channel_name='{self.channel_name}')>"

    def __str__(self):
        return f"Channel: {self.channel_name} (ID: {self.channel_id})"

    schedule_id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(String, ForeignKey('users.phone_number'))
    channel_id = Column(Integer, ForeignKey('channels.channel_id'))

    user = relationship('User', back_populates='custom_schedules')
    channel = relationship('Channel')
