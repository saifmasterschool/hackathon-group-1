from sqlalchemy import Column, Integer, String, DateTime, func

from database.extension import Base


class Jokes(Base):
    __tablename__ = "jokes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    joke = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
