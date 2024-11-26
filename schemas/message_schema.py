from sqlite_manager import Base

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship


class Jokes(Base):
    __tablename__ = "jokes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sender = Column(Integer, nullable=False)
    message = Column(String, nullable=False)
    receivedAt = Column(DateTime, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
