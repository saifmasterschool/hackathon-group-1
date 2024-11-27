from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database.extension import Base


class CustomSchedule(Base):
    __tablename__ = 'custom_schedules'

    schedule_id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(String, ForeignKey('users.phone_number'))
    channel_id = Column(Integer, ForeignKey('channels.channel_id'))

    user = relationship('User', back_populates='custom_schedules')
    channel = relationship('Channel')
