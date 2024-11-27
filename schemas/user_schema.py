from sqlalchemy import Column, Integer, JSON, DateTime, func
from sqlalchemy.ext.hybrid import hybrid_method

from database.extension import Base


class User(Base):
    __tablename__ = "users"

    phone_number = Column(Integer, primary_key=True, nullable=False)
    channels = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    @hybrid_method
    def has_channel(self, channel):
        return channel in self.channels
