from sqlalchemy import Column, Integer, String, DateTime, func

from database.extension import Base


class Message(Base):
    __tablename__ = "messages"

    def __repr__(self):
        return f"<Message(id={self.id}, sender={self.sender}, message='{self.message}', receivedAt='{self.receivedAt}', created_at='{self.created_at}', updated_at='{self.updated_at}')>"

    def __str__(self):
        return f"Message from {self.sender}: {self.message} (Received at: {self.receivedAt}, Created at: {self.created_at}, Updated at: {self.updated_at})"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sender = Column(Integer, nullable=False)
    message = Column(String, nullable=False)
    receivedAt = Column(DateTime, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
