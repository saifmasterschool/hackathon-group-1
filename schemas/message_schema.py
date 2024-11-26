from sqlalchemy import Column, Integer, String, DateTime, func

from database.extension import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sender = Column(Integer, nullable=False)
    message = Column(String, nullable=False)
    receivedAt = Column(DateTime, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
