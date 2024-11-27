from sqlalchemy import Column, Integer, String, DateTime, func

from database.extension import Base


class Jokes(Base):
    __tablename__ = "jokes"

    def __repr__(self):
        return f"<Joke(id={self.id}, joke='{self.joke}', created_at='{self.created_at}', updated_at='{self.updated_at}')>"

    def __str__(self):
        return f"Joke: {self.joke} (ID: {self.id}, Created at: {self.created_at}, Updated at: {self.updated_at})"

    id = Column(Integer, primary_key=True, autoincrement=True)
    joke = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
