from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.ext.hybrid import hybrid_method
from sqlalchemy.orm import relationship

from database.extension import Base


class User(Base):
    __tablename__ = "users"

    phone_number = Column(Integer, primary_key=True, nullable=False)

    subscriptions = relationship('Subscription', back_populates='user')
    channels = relationship('Channel', secondary='subscriptions', viewonly=True)
    custom_schedules = relationship('CustomSchedule', back_populates='user')

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    @hybrid_method
    def has_channel(self, channel):
        return channel in self.channels

    @hybrid_method
    def has_custom_schedule(self, channel):
        return channel in self.custom_schedules
