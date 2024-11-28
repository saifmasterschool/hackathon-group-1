from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from utils.to_dict_mixin_schema import ToDictMixin

from database.extension import Base


class CustomSchedule(Base, ToDictMixin):
    __tablename__ = 'custom_schedules'

    schedule_id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(String, ForeignKey('users.phone_number'))
    channel_id = Column(Integer, ForeignKey('channels.channel_id'))
    schedule = Column(String, nullable=False)

    user = relationship('User', back_populates='custom_schedules', lazy="joined")
    channel = relationship('Channel', lazy="joined")
